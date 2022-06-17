import pandas as pd
import numpy as np
import math
# to readd files 
data_train = pd.read_csv('lab_final\\train.csv')
data_test = pd.read_csv('lab_final\\test.csv')
# to get words and turn it into list
# words_train [] is the words list for train_set.csv, and according to the demand, it should be train_set && validation_set, anyway, just change the fle source
col_word = data_train['sentence']
words = np.array(col_word)
array_label = data_train['gold_label']
array_test = data_test['gold_label']
# trash_words = ['the','a','an','of','that','"','it','which','for','and']

# def get_rid_of(sentence):
#     for i in range(len(words)):
#         for j in range(len(sentence[i])):
#             if sentence[i][j] in trash_words:
#                 sentence[i][j] = '' # is that available ?

# 最终的括号套括号的表达形式
words_train = []
for i in range(len(words)):
    index = words[i].split()
    words_train.append(index)

Len_words = len(words)
# the baseline
K = int(math.sqrt(Len_words))
# to create corpus
corpus = []
for i in range(Len_words):
    for j in range(len(words_train[i])):
        if words_train[i][j] not in corpus:
            corpus.append(words_train[i][j])
len_corpus = len(corpus)

# One-hot
# Noromally, it should include test_set's corpus, but i didn't use the COS to cauclate the distance so i simplified it.
One_hot = []
for i in range(len(words)):
    index = [0 for n in range(len_corpus)]
    for j in range(len(words_train[i])):
        index_position = corpus.index(words_train[i][j])
        index[index_position] += 1
    One_hot.append(index)

# The classic KNN with Eulic-distance
def Eucli_distance_KNN(str):
    # the sum of each emotion
    lable = [0,0,0,0,0,0]
    distance = []
    # as i mentioned before, I used a (not_in_corpus) to get extra distance
    not_in_corpus = 0
    # str's one-hot
    index = [0 for n in range(len_corpus)]
    for j in range(len(str)):
        if str[j] in corpus:
            index_position = corpus.index(str[j])
            index[index_position] += 1
        else: # if it's not in corpus, count 1
            not_in_corpus += 1
    array_train = array_label
    # distance and emotion
    for i in range(Len_words):
        # get rid of the trouble to cauclate test's corpu
        # Eulic distance^2
        Eulic = not_in_corpus
        for j in range(len_corpus):
            Eulic += math.pow(One_hot[i][j] - index[j],2)
        index_distance = math.sqrt(Eulic)
        # get distace and emotion in the meantime
        distance.append((index_distance,array_train[i]))
    # to get first Kst
    distance.sort(key=lambda x:x[0])
    for j in range(K+1):
        lable[distance[j][1]] += 1
    # return the max's lable
    return lable.index(max(lable))

if __name__=='__main__':
    col_word = data_test['sentence']
    words = np.array(col_word)
    words_test = []
    for i in range(len(words)):
        index = words[i].split()
        words_test.append(index)
    N1 = len(words_test)
    emotion_new = []
    index_true = 0
    for i in range(len(col_word)): 
        emotion_new.append(Eucli_distance_KNN(words_test[i]))
        if emotion_new[i] == array_test[i]:
            index_true += 1
    print(emotion_new)
    print('accurry:',format(index_true*1.0/len(col_word),'.10f'))