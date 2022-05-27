# # import csv
# # result = []
# # with open('AI\\lab6\\train_set.csv', 'r') as f:
# #     r = csv.reader(f, delimiter=',')
# #     # next(r, None) # skip the headers
# #     for row in r:
# #         result.append(row)
# #     print(result)
# # ll=[95,68,93,89,98,100,73,78,88,85,101,200]
# # ll.sort(reverse=True)
# # print(ll)
import re
import pandas as pd
import csv
import numpy as np

# # a full set inluding 'test_set.csv' and 'validation_set.csv'
# data_train = pd.read_csv('AI\\lab6\\final_set.csv')
# # test_set.csv
# data_test = pd.read_csv('AI\\lab6\\test_set.csv')

# col_word = data_train['Words']
# words = np.array(col_word)
# words_train = []
# for i in range(len(words)):
#     index = words[i].split()
#     words_train.append(index)
# #print(words_train)

# anger_train = np.array(data_train['anger'])
# disgust_train = np.array(data_train['disgust'])
# fear_train = np.array(data_train['fear'])
# joy_train = np.array(data_train['joy'])
# sad_train = np.array(data_train['sad'])
# surprise_train = np.array(data_train['surprise'])
# # to find emotion
# emotion_train = []
# N = len(words_train)
# for i in range(N):
#     emotion_train.append([anger_train[i],disgust_train[i],fear_train[i],joy_train[i],sad_train[i],surprise_train[i]])
# # to find emotion type [0,5]
# emo_array = []
# for i in range(N):
#     index = emotion_train[i].index(max(emotion_train[i]))
#     emo_array.append(index)


# 语料库长这样：
# import numpy as np
# import pandas as pd 

# text = ['Today is Friday it is Sunny',
#        'Yesterday is Thursday it was cloudy']
# # 先分词处理
# text = [s.split() for s in text]
# text = pd.Series(text)
# # 第一行文本，每个单词的 one-hot 表示
# text1 = pd.get_dummies(text)
# print(text1)
# print(text1.shape)

# x =[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
# y = [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
# print(x[1][2])
with open('20337268_zhangwenqin_NB_classification.csv', 'w') as f:
    # 创建writer
    writer = csv.writer(f)
    str = 'hello'
    writer.writerow(str)



    for i in range(Len_words):
        Eulic = not_in_corpus
        for j in range(len_corpus):
            Eulic += math.pow(One_hot[i][j] - index[j],1)
            len_a = 
        #index_distance = math.sqrt(Eulic)
        #distance.append(index_distance)
        distance.append(Eulic)
    distance.sort()