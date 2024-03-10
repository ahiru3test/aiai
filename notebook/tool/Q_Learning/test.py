import random

# WALL = 0    # 壁
# ROAD = 1    # 通路
# WAY = 2     # 通った経路

# MAZE_SIZE = 60
# MAZE_NUM = 5

# maze = []
# for y in range(MAZE_NUM):
#     maze.append([0]*MAZE_NUM)


# def make_maze():
#     XP = [0, 1, 0, -1]
#     YP = [-1, 0, 1, 0]

#     # ボードの周囲を壁にする
#     for x in range(MAZE_NUM):
#         maze[0][x] = WALL
#         maze[MAZE_NUM-1][x] = WALL
#     for y in range(MAZE_NUM-1):
#         maze[y][0] = WALL
#         maze[y][MAZE_NUM-1] = WALL

#     # ボードの中を全て通路にする
#     for y in range(1, MAZE_NUM-1):
#         for x in range(1, MAZE_NUM-1):
#             maze[y][x] = ROAD

#     # 棒倒し法
#     for y in range(2, MAZE_NUM-2, 2):
#         for x in range(2, MAZE_NUM-2, 2):
#             maze[y][x] = WALL
#     for y in range(2, MAZE_NUM-2, 2):
#         for x in range(2, MAZE_NUM-2, 2):
#             d = random.randint(0, 3)
#             if x > 2:
#                 d = random.randint(0, 2)
#             maze[y+YP[d]][x+XP[d]] = WALL

# make_maze()
# for i in range(MAZE_NUM): print(maze[i])

# #---
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0]
# [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0]
# [0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0]
# [0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0]
# [0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0]
# [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0]
# [0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0]
# [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
# [0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# #---
#---

# 与えられた迷路設定
maze = [[0,0,0,0,0], # 0- 4
        [0,1,1,1,0], # 5- 9
        [0,1,0,0,0], #10-14
        [0,1,1,9,0], #15-19
        [0,0,0,0,0]] #20-24

#---------#---------#---------#---------#---------#---------#---------#-
import numpy as np

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

# 与えられた迷路設定 [1][1],[3][1],[1][3],[3][3]
maze = [[0,0,0,0,0], # 0- 4
        [0,1,1,1,0], # 5- 9
        [0,1,0,0,0], #10-14
        [0,1,1,9,0], #15-19
        [0,0,0,0,0]] #20-24

# 報酬設定を作成
reward_setting = create_reward_setting(maze)
print(reward_setting)
#---------#---------#---------#---------#---------#---------#---------#-
