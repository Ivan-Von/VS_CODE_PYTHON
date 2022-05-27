import sys
import copy
import heapq
import numpy as np
import time
#目标状态
end_state = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0)
#初始状态
init_state = [
     (1, 2, 4, 8, 5, 7, 11, 10, 13, 15, 0, 3, 14, 6, 9, 12),
     (5,1,3,4,2,7,8,12,9,6,11,15,0,13,10,14),
     (14,10,6,0,4,9,1,8,2,3,5,11,12,13,7,15),
     (6,10,3,15,14,8,7,11,5,1,0,2,13,12,9,4)
]

dx = [0,-1,0,1]
dy = [1,0,-1,0]

def __cut__():#设计剪枝函数
    
def __fx__():#设计f(x)和h(x)g(x)


def read(filePath):
    with open(filePath, encoding='utf-8') as file_obj:
        for line in open(filePath,encoding='utf-8'):
            value = list(map(int,line.split()))
            B.append(value)
def __main__():
    filePath = r'Maze.txt'
    read(filePath)
    print(B)