# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 17:45:37 2018
@author: ck
"""

'''
update:
    估值函数为权值表+行动力+稳定子
    对于较顶层节点使用一步预搜索获得估值排序后的前maxN个最优操作,限制搜索宽度并尽量提前剪枝
test:
    潜在行动力无助于提升性能
'''
import string
import json
import numpy

DIR = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)) # 方向向量，周围八个方向

# 放置棋子，计算新局面
def place(board, x, y, color):
    if x < 0 or y < 0:
        return False
    board[x][y] = color
    valid = False
    for d in range(8):
        i = x + DIR[d][0]
        j = y + DIR[d][1]
        while 0 <= i and i < 8 and 0 <= j and j < 8 and board[i][j] == -color:
            i += DIR[d][0]
            j += DIR[d][1] 
        if 0 <= i and i < 8 and 0 <= j and j < 8 and board[i][j] == color:
            while True:
                i -= DIR[d][0]
                j -= DIR[d][1]
                if i == x and j == y:
                    break
                valid = True
                board[i][j] = color
    return valid

def getmoves(board, color): #行动力
    moves = []
    ValidBoardList = []
    for i in range(8):
        for j in range(8):
            if board[i][j] == 0:
                newBoard = board.copy()
                if place(newBoard, i, j, color):
                    moves.append((i, j))
                    ValidBoardList.append(newBoard)
    return moves, ValidBoardList


Vmap = numpy.array([[500,-25,10,5,5,10,-25,500],
                    [-25,-45,1,1,1,1,-45,-25],
                    [10,1,3,2,2,3,1,10],
                    [5,1,2,1,1,2,1,5],
                    [5,1,2,1,1,2,1,5],
                    [10,1,3,2,2,3,1,10],
                    [-25,-45,1,1,1,1,-45,-25],
                    [500,-25,10,5,5,10,-25,500]])

    
def mapweightsum(board, mycolor): #位置权值
    return sum(sum(board*Vmap))*mycolor

def evaluation(moves, board, mycolor): #估值函数
    moves_, ValidBoardList_ = getmoves(board, -mycolor)
    #stable = getstable(board, mycolor)
    value = mapweightsum(board, mycolor) + 15*(len(moves)-len(moves_))
    # + 10*sum(stable)
    return value

def onestepplace(board, mycolor):
    stage = sum(sum(abs(board)))
    if stage <= 9:
        depth = 5
    elif stage >= 50:
        depth = 6
    else:
        depth = 4
    value, bestmove = alphabetav2(board, depth, -10000, 10000, mycolor, mycolor, depth)
    return bestmove

def alphabetav2(board, depth, alpha, beta, actcolor, mycolor, maxdepth):
    moves, ValidBoardList = getmoves(board, actcolor)
    if len(moves) == 0:
        return evaluation(moves, board, mycolor), (-1, -1)
    if depth == 0:
        return evaluation(moves, board, mycolor), []
    
    if depth == maxdepth:
        for i in range(len(moves)):
            if Vmap[moves[i][0]][moves[i][1]] == Vmap[0][0] and actcolor == mycolor:
                return 1000, moves[i]
                
    #对于较顶层节点使用一步预搜索获得估值排序后的前maxN个最优操作，限制搜索宽度并尽量提前剪枝
    if depth >= 4:
        Vmoves = []
        for i in range(len(ValidBoardList)):
            value, bestmove = alphabetav2(ValidBoardList[i], 1, -10000, 10000, -actcolor, mycolor, maxdepth)
            Vmoves.append(value)
        ind = numpy.argsort(Vmoves)
        maxN = 6
        moves = [moves[i] for i in ind[0:maxN]]
        ValidBoardList = [ValidBoardList[i] for i in ind[0:maxN]]
    
    bestmove = []
    bestscore = -10000
    for i in range(len(ValidBoardList)):
        score, childmove = alphabetav2(ValidBoardList[i], depth-1, -beta, -max(alpha, bestscore), -actcolor, mycolor, maxdepth)
        score = -score
        if score > bestscore:
            bestscore = score
            bestmove = moves[i]
            if bestscore > beta:
                return bestscore, bestmove
    return bestscore, bestmove

def end(board):
    for i in range(8):
        for j in range(8):
            if board[i][j] == 0:
                return True
    return False

board = numpy.zeros((8,8),dtype=numpy.int)
board[3][4] = board[4][3] = 1 #白
board[3][3] = board[4][4] = -1 #黑
AIColor = 1

while(end(board)):
    move = onestepplace(board,AIColor)
    x,y = move
    print("The AI chosed :",move)
    place(board,x,y,1)
    print("After AI, the score is:",sum(sum(board)),"\nand the board is:")
    print(board)
    moves = getmoves(board,-AIColor)
    print("Your choice:")
    print(moves[0])
    if moves[0] == []:
        input("No place to go")
        continue
    else:
        i = input("Where to go")
        if not i.isdigit():
            print("WARNING! IILEGAL INPUT. YOU LOST AN CHANCE!")
        elif int(i) >= len(moves[0]) or int(i) < 0:
            print("WARNING! IILEGAL INPUT. YOU LOST AN CHANCE!")
        else:
            yourmove = moves[0][int(i)]
            place(board,yourmove[0],yourmove[1],-AIColor)
            print("After You, the score is:",sum(sum(board)),"\nand the board is:")
            print(board)

score = sum(sum(board))
if(score < 0):
    print("You win")
elif score == 0:
    print("DEUCE")
else:
    print("You lost")