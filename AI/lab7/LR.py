# Notice that the w and x are 41 dimensions.
import numpy as np
import pandas as pd
import math
import csv

data_train = pd.read_csv('AI\\lab7\\train.csv')
test_train = pd.read_csv('AI\\lab7\\test.csv')

x = np.array(data_train)

# change set answer into 1
for i in range(len(x)):
    x[i][40] = 1

answer = data_train['answer']

# from the beginning, just set it into 1 
need = [1 for i in range(len(x))]

# n + 1 dimensions vector
w = [0 for i in range(41)]
# it is b
w[40] = 1
# 学习率
n = 0.5

def pi(j):
    sum = 0
    # to cancluate w*x
    for i in range(41):
        sum += w[i]*x[j][i]
    # in pi(x), we need this P instead of the other one.
    P = 1.0/(1+math.exp(-sum))
    return P

# def __get_P__(index,j):
#     P = pi(j)
#     #P = math.exp(sum)*1.0 / (1+math.exp(sum))
#     if index == 1:
#         return P
#     elif index == 0:
#         return 1-P
#     else:
#         print("what's wrong with you?")
#         return -1

# # 对数似然函数
def L():
    L = 0
    for i in range(len(x)):
        sum = 0
        for j in range(41):
            sum += x[i][j]*w[j]
        L += (answer[i]*sum - math.log(1 + math.exp(sum)))

# # seems it's of no use
# def __logistic__(x):
#     return 1.0/(1+math.exp(-x))

# I get it from the following functions

# def get_step():
#     for i in range(len(x)):
#         rate = 0
#         rate  = (answer[i] - pi(i))
#         for j in range(41):
#             update = 

# to update w

def update_w():
    update = [0 for i in range(41)]
    for i in range(len(x)):
        rate = 0
        rate = (answer[i] - pi(i))
        for j in range(41):
            update[j] += rate * x[i][j]
    for i in range(41):
        w[i] += n * update[i]

def update_need():
    for i in range(len(x)):
        if (pi(i) > 1/2 and answer[i] == 1) or (pi(i) < 1/2 and answer[i] == 0):
            need[i] = 0
        else:
            need[i] = 1

if __name__ ==  '__main__':
    print(w)
    update_need()
    while(1 in need):
        update_w()
        print(w)
        update_need()
