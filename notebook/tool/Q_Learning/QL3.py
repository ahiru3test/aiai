import numpy as np #----------------------------------------------------
gamma, alpha = 0.9, 0.1 #将来価値の割引(低い程利益重視)と学習率を設定。
array_num, goal_val=3, 65535 #n*n迷路arrayのサイズとゴールの価値(>10000)
reward = np.array([[0,1,0,1,0,0,0,0,0], #迷路 S────┐
                   [1,0,1,0,1,0,0,0,0], #012 │0 1 _│
                   [0,1,0,0,0,0,0,0,0], #345 │3│4 5│
                   [1,0,0,0,0,0,1,0,0], #678 │6 7│8│
                   [0,1,0,0,0,1,0,1,0], #    └───┘G
                   [0,0,0,0,1,0,0,0,9],
                   [0,0,0,1,0,0,0,1,0],
                   [0,0,0,0,1,0,1,0,0],
                   [0,0,0,0,0,1,0,0,0]]) #報酬設定(1=移動可能,9=ゴール)
reward[np.where(reward == 9)] = 65535 #報酬9をゴール報酬に置き換える
Q = np.zeros([array_num**2, array_num**2]) #Q値の初期値を0に設定

for _ in range(10000): #とりあえず1万回Q学習しランダムに位置・行動を選択
    p_state = np.random.randint(0, array_num**2) #現在位置をランダム選択
    #以下のコードはreward[p_state]の要素が1以上のインデックスを取る。
    #[0]は戻り値タプルの最初の要素だけを取るためのインデックス指定です。
    n_actions = np.where(reward[p_state] >= 1)[0] #次の行動の候補
    n_state = np.random.choice(n_actions) #行動可能候補からランダム選択
    
    #Q値の更新。学習率が小さいほど現在の行動価値重視。更新が抑え目になる
    #ここでQ学習に用いる「たった一つの数式」で行動価値を学習していく
    Q[p_state, n_state] = (1-alpha)*Q[p_state, n_state]+alpha*(
        reward[p_state,n_state]+gamma*Q[n_state,np.argmax(Q[n_state])])

def shortest_path(start,reward,Q): #最短ルート表示。Q値の最高値をappend
    path = [start] #pathに経路を追加していく
    while path[-1] != np.argmax(reward)%(array_num**2): #ゴールまで選択
        path.append(np.argmax(Q[path[-1]])) #経路をpathに追加
    
    return path

print(shortest_path(0,reward,Q)) #スタートを0として最短経路を表示
