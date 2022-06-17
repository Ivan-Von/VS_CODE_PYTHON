# -*- coding: utf-8 -*-
# @Time    : 2022/6/2
# @Author  : Ivan-Von
# @FileName: main.py
# @Software: vscode
# @Blog    ：github.com @Ivan-Von
# contain: design a program to decide truth or not.

# deal_data.py : to get rid of some unecessary words and change them into a bag of words or something.
from read import*
import string
# need expanding
trash_words = ['the','a','an','of','that','"','it','which']

def get_rid_of():
    for i in range(len(x)):
        for j in range(len(sentence[i])):
            if sentence[i][j] in trash_words:
                sentence[i][j] = '' # is that available ?

def divid():
    return

remove = str.maketrans('','',string.punctuation) 
data = data.translate(remove)
