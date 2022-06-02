import pandas as pd
import numpy as np
data_train = pd.read_csv('AI\\lab7\\train.csv')
test_train = pd.read_csv('AI\\lab7\\test.csv')
x = np.array(data_train)
answer = data_train['answer']
LEN = 7000
n = 1
w = [0 for i in range(40)]
b = 0
need = [1 for i in range(LEN)]

def update_need():
    for i in range(LEN):
        if identify(i):
            need[i] = 1
        else:
            need[i] = 0

def update_wb():
    i = need.index(1)
    for j in range(40):
        w[j] += n*x[i][j]*answer[i]
    global b
    b += n* answer[i]

def identify(j):
    sum = 0
    for i in range(40):
        sum += w[i]*x[j][i]
    sum += b
    # 1 presents needy 
    if (sum > 0 and answer[j] == 0) or (sum <=0 and answer[j] == 1):
        return 1
    elif (sum  <= 0 and answer[i] == 0) or (sum > 0 and answer[i] == 1):
        return 0

if __name__ == '__main__':
    update_need()
    i = 0
    print(w,b)
    while 1 in need:
        i += 1
        print(i)
        if i > 8:
            break
        else:
            update_wb()
            print(w,b)
    right = 0
    for j in range(1000):
        if(not identify(j+LEN)):
            right += 1
    print(right*1.0/1000)