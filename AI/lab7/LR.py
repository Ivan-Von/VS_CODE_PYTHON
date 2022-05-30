import numpy as np
import pandas as pd
import csv
data_train = pd.read_csv('AI\\lab7\\train.csv')
test_train = pd.read_csv('AI\\lab7\\test.csv')
x = np.array(data_train)
# chenge it into 1 all
for i in range(len(x)):
    x[i][40] = 1
answer = data_train['answer']
def update():
def __logistic__():
