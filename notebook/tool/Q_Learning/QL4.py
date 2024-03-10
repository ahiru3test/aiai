import numpy as np #----------------------------------------------------
import random

WALL = 0    # 壁
ROAD = 1    # 通路
WAY = 2     # 通った経路
MAZE_NUM = 31

# ******************** 棒倒し方による迷路の自動生成 ********************
def make_maze(maze):
    XP = [0, 1, 0, -1]
    YP = [-1, 0, 1, 0]

    # 周囲を壁にする
    for x in range(MAZE_NUM):
        maze[0][x] = WALL
        maze[MAZE_NUM-1][x] = WALL
    for y in range(MAZE_NUM-1):
        maze[y][0] = WALL
        maze[y][MAZE_NUM-1] = WALL

    # 中を全て通路にする
    for y in range(1, MAZE_NUM-1):
        for x in range(1, MAZE_NUM-1):
            maze[y][x] = ROAD

    # 棒倒し法
    for y in range(2, MAZE_NUM-2, 2):
        for x in range(2, MAZE_NUM-2, 2):
            maze[y][x] = WALL
    for y in range(2, MAZE_NUM-2, 2):
        for x in range(2, MAZE_NUM-2, 2):
            d = random.randint(0, 3)
            if x > 2:
                d = random.randint(0, 2)
            maze[y+YP[d]][x+XP[d]] = WALL

# ******************** 報酬設定 ****************************************
def create_reward_setting(maze):
    rows, cols = len(maze), len(maze[0]) # 迷路のサイズを取得
    reward_setting = np.zeros(
        (rows * cols, rows * cols), dtype=int) # 報酬設定の配列を作成

    # 迷路の各セルに対して報酬設定を行う
    for i in range(rows):
        for j in range(cols):
            if maze[i][j] == 1 or maze[i][j] == 9:  # 移動可能orゴール
                index = i * cols + j
                set_num = 1
                # 上
                if i > 0 and maze[i-1][j] > 0:
                    if maze[i-1][j] == 9: set_num =9
                    reward_setting[index][index-cols] = set_num
                # 下
                if i < rows-1 and maze[i+1][j] > 0:
                    if maze[i+1][j] == 9: set_num =9
                    reward_setting[index][index+cols] = set_num
                # 左
                if j > 0 and maze[i][j-1] > 0:
                    if maze[i][j-1] == 9: set_num =9
                    reward_setting[index][index-1] = set_num
                # 右
                if j < cols-1 and maze[i][j+1] > 0:
                    if maze[i][j+1] == 9: set_num =9
                    reward_setting[index][index+1] = set_num
    return reward_setting

# ----------------------------------------------------------------------

def shortest_path(start,reward,Q): #最短ルート表示。Q値の最高値をappend
    path = [start] #pathに経路を追加していく
    while path[-1] != np.argmax(reward)%(MAZE_NUM**2): #ゴールまで選択
        path.append(np.argmax(Q[path[-1]])) #経路をpathに追加
    
    return path

if(__name__!="__main__"): exit()

# gamma, alpha = 0.9, 0.1 #将来価値の割引(低い程利益重視)と学習率を設定。
gamma, alpha = 0.5, 0.8 #将来価値の割引(低い程利益重視)と学習率を設定。
goal_val=999999999 #n*n迷路arrayのサイズとゴールの価値
corner=MAZE_NUM-2 #四隅の座標
maze = [[0] * MAZE_NUM for _ in range(MAZE_NUM)]
make_maze(maze) # 迷路設定

rnd1,rnd2=1,1
while(rnd1*rnd2<=1) :
    rnd1,rnd2=random.choice([1,corner]),random.choice([1,corner])
maze[rnd1][rnd2]=9
# maze[corner][corner] = 9


for i in range(MAZE_NUM): print(maze[i])


reward = np.array(create_reward_setting(maze))
# for i in range(MAZE_NUM**2):print(reward[i])

# reward_setting = create_reward_setting(maze)
# print(reward_setting)


# reward = np.array([[0,1,0,1,0,0,0,0,0], #迷路 S────┐
#                    [1,0,1,0,1,0,0,0,0], #012 │0 1 _│
#                    [0,1,0,0,0,0,0,0,0], #345 │3│4 5│
#                    [1,0,0,0,0,0,1,0,0], #678 │6 7│8│
#                    [0,1,0,0,0,1,0,1,0], #    └───┘G
#                    [0,0,0,0,1,0,0,0,9],
#                    [0,0,0,1,0,0,0,1,0],
#                    [0,0,0,0,1,0,1,0,0],
#                    [0,0,0,0,0,1,0,0,0]])#報酬設定(1=移動可能,9=ゴール)
reward[np.where(reward == 9)] = goal_val #報酬9をゴール報酬に置き換える
Q = np.zeros([MAZE_NUM**2, MAZE_NUM**2]) #Q値の初期値を0に設定

# ----------------------------------------------------------------------
non=set()
for _ in range(500000): #50万回Q学習しランダムに位置・行動を選択
    loop = True
    while loop:
        p_state = np.random.randint(0, MAZE_NUM**2) #ランダムな現在位置
        if p_state in non: continue
        #以下のコードはreward[p_state]の要素が1以上のインデックスを取る
        #[0]は戻り値タプルの最初の要素だけを取るためのインデックス指定
        n_actions = np.where(reward[p_state] >= 1)[0] #次の行動の候補
        if len(n_actions) > 0:
            loop=False
        else:
            non.add(p_state)
    n_state = np.random.choice(n_actions) #行動可能候補からランダム選択
    
    #Q値の更新。学習率が小さいほど現在の行動価値重視。更新が抑え目になる
    #ここでQ学習に用いる「たった一つの数式」で行動価値を学習していく
    Q[p_state, n_state] = (1-alpha)*Q[p_state, n_state]+alpha*(
        reward[p_state,n_state]+gamma*Q[n_state,np.argmax(Q[n_state])])


print("shortest path:",shortest_path(MAZE_NUM+1,reward,Q)) #最短経路
# for i in range(MAZE_NUM): print(maze[i],",") #迷路設定を表示
# print(non)
