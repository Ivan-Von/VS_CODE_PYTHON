import numpy as np
import pandas as pd
import math
data_train = pd.read_csv('AI\\lab7\\train.csv')
test_train = pd.read_csv('AI\\lab7\\test.csv')
x = np.array(data_train)
for i in range(len(x)):
    x[i][40] = 1
answer = data_train['answer']
need = [1 for i in range(len(x))]
w = [0 for i in range(41)]
n = 100

def pi(j):
    sum = 0
    for i in range(41):
        sum += w[i]*x[j][i]
    if sum > 10:
        P = 0
    elif sum < -10:
        P = 1
    else:
        P = 1.0/(1+math.exp(-sum))
    return P

def update_w():
    update = [0 for i in range(41)]
    rate = 0
    for i in range(len(x)):
        rate = answer[i] - pi(i)
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

def L():
    L = 0
    for i in range(len(x)):
        sum = 0
        for j in range(41):
            sum += x[i][j]*w[j]
        if sum > 10:
            sum = 10
        elif sum < -10:
            sum = -10
        else:
            sum = sum
        L += (answer[i]*sum - math.log(1 + math.exp(sum)))
    return L

if __name__ ==  '__main__':
    print(w)
    update_need()
    print(need)
    print(L())
    i = 0
    while(1 in need):
        i += 1
        if i > 100:
            break
        update_w()
        print(w)
        update_need()
        print(need)
        print(L())