# -*- coding: utf-8 -*-
# @Time    : 2022/6/2
# @Author  : Ivan-Von
# @FileName: main.py
# @Software: vscode
# @Blog    ：github.com @Ivan-Von
# contain: design a program to decide truth or not.

# read.py : to read file
import numpy as np
import pandas as pd
data_train = pd.read_csv('lab_final\\train.csv')
x = np.array(data_train)
# sentenceID,gold_label,sentence
sentenceID = data_train['sentenceID']
gold_lable = data_train['gold_lable']
sentence = data_train['sentence']