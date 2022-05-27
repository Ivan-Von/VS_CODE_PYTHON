from evaluation import*
from new_board import*
import numpy
import math
from random import random
from alpha_beta import Alpha_Beta

# SA algorithm
# Function for evaluating 
def drop_fun(color,board):
    return sum(sum(board * Vmap))*color

# to get a random point
def generate_new(x, y, T,board,color):
    moves,_ = execution(board, color)
    while True:
        x_new = int(x + T * (random() - random())*9)
        y_new = int(y + T * (random() - random())*9)
        if((x,y) in moves):
            break
    return x_new,y_new

# To determain whether legal or not
def Metrospolis(f, f_new,T):
    if(f_new < f):
        return 1
    else:
        p = math.exp((f-f_new)/T)
        if random()<p:
            return 1
        else:
            return 0

# The body
def run(board,depth,alpha,beta,actcolor,mycolor,maxdepth,T=100,Tf=1):
    bestmove = []
    moves,ValidBoardList = execution(board, actcolor)
    if len(moves) == 0:
        return evaluation(moves,board,mycolor),(-1,-1)
    if depth == 0:
        return evaluation(moves,board,mycolor),[]
    if depth == maxdepth:
        for i in range(len(moves)):
            if Vmap[moves[i][0]][moves[i][1]] == Vmap[0][0] and actcolor == mycolor:
                return 1000,moves[i]
        if depth >= 4:
            V_value = []
            for i in range(len(ValidBoardList)):
                value, _ = Alpha_Beta(ValidBoardList[i], 1, -10000, 10000, -actcolor, mycolor, maxdepth)
            V_value.append(value)
        ind = numpy.argsort(V_value)
        maxN = 6
        moves = [moves[i] for i in ind[0:maxN]]
        ValidBoardList = [ValidBoardList[i] for i in ind[0:maxN]]
    while T > Tf:
        moves,ValidBoardList = execution(board, actcolor)
        for i in range(len(ValidBoardList)):
            score = evaluation(moves,ValidBoardList[i],mycolor)
            x_new,y_new = generate_new(moves[i][0],moves[i][1],T,board,actcolor)
            score_new = generate_new(x_new,y_new,T,board,actcolor)
            if Metrospolis(score,score_new,T):
                bestmove.append((x_new,y_new))
        T = T * 0.1
    bestscore = -10000
    for i in range(len(ValidBoardList)):
        score, _ = Alpha_Beta(ValidBoardList[i], depth-1, -beta, -max(alpha, bestscore), -actcolor, mycolor, maxdepth)
        score = -score
        if score > bestscore:
            bestscore = score
            bestmove = moves[i]
            if bestscore > beta:
                return bestscore, bestmove
    return bestscore, bestmove