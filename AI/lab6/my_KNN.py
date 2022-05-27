import pandas as pd
import numpy as np
import math
import csv
emotion = {0:"anger",1:"disgust",2:"fear",3:"joy",4:"sad",5:"surprise"}
# to readd files 
data_train = pd.read_csv('AI\\lab6\\train_set.csv')
data_test = pd.read_csv('AI\\lab6\\test_set.csv')
data_validation = pd.read_csv('AI\\lab6\\validation_set.csv')

# to get words and turn it into list
# words_train [] is the words list for train_set.csv, and according to the demand, it should be train_set && validation_set, anyway, just change the fle source
col_word = data_train['Words']
words = np.array(col_word)
words_train = []
for i in range(len(words)):
    index = words[i].split()
    words_train.append(index)

Len_words = len(words)

# the baseline
K = int(math.sqrt(Len_words))
#K = int(Len_words/20)
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

# to get emotion
def get_emotion(data_train,N):
    # get emotions
    anger_train = np.array(data_train['anger'])
    disgust_train = np.array(data_train['disgust'])
    fear_train = np.array(data_train['fear'])
    joy_train = np.array(data_train['joy'])
    sad_train = np.array(data_train['sad'])
    surprise_train = np.array(data_train['surprise'])
    # to find emotion
    emotion_train = []
    for i in range(N):
        emotion_train.append([anger_train[i],disgust_train[i],fear_train[i],joy_train[i],sad_train[i],surprise_train[i]])
    # to find emotion type [0,5]
    emo_array = []
    for i in range(N):
        index = emotion_train[i].index(max(emotion_train[i]))
        emo_array.append(index)
    return emotion_train,emo_array
    # the 1st return is 6 emotions, 2nd return is sentences' emotions

# to cauclate the accuracy
def compare_(emo_array1,emo_array2):
    index = 0
    for i in range(len(emo_array1)):
        if emo_array1[i] == emo_array2[i]:
            index += 1
    print("The accuracy is :",round(index*1.0/len(emo_array1),10)) 

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
    _,emotion_train = get_emotion(data_train,Len_words)
    # distance and emotion
    for i in range(Len_words):
        # get rid of the trouble to cauclate test's corpus

        # Eulic distance^2
        Eulic = not_in_corpus
        for j in range(len_corpus):
            Eulic += math.pow(One_hot[i][j] - index[j],2)
        index_distance = math.sqrt(Eulic)
        # get distace and emotion in the meantime
        distance.append((index_distance,emotion_train[i]))
    # to get first Kst
    distance.sort(key=lambda x:x[0])
    for j in range(K+1):
        lable[distance[j][1]] += 1
    # return the max's lable
    return lable.index(max(lable))

# The regressive KNN with Eulic distance
def Eucli_distance_KNN_regression(str):
    lable = [0,0,0,0,0,0]
    distance = []
    not_in_corpus = 0
    index_str = [0 for n in range(len_corpus)]
    index = [0 for n in range(len_corpus)]
    for j in range(len(str)):
        if str[j] in corpus:
            index_position = corpus.index(str[j])
            index[index_position] += 1
        else:
            not_in_corpus += 1
    # in regressive KNN, we just need all 6 emotions
    all_emotion,_ = get_emotion(data_train,Len_words)

    # 欧式距离和曼哈顿距离

    # for i in range(Len_words):
    #     Eulic = not_in_corpus
    #     for j in range(len_corpus):
    #         Eulic += math.pow(One_hot[i][j] - index[j],2)
    #     index_distance = math.sqrt(Eulic)
    #     distance.append(index_distance)
    # distance.sort()
    
    # 余弦相似度

    # for i in range(Len_words):
    #     len_A = 0
    #     len_B = 0
    #     product = 0
    #     for j in range(len(words[i])):
    #         # to get each sentecne's vector
    #         index_str[corpus.index(j)] += 1
    #     for k in range(corpus):
    #         # to get sentence's length
    #         len_A += index_str[k]
    #         # to get sentence(waiting for verification)'s length
    #         len_B += index[k]
    #         # to get their product
    #         product += index[k] * index_str[k]
    #     distance.append(1-(product*1.0)/(len_A*len_B*1.0))
    # distance.sort()

    # Jaccard相似度

    for i in range(Len_words):
        # because we have known the sum of words that are not in the corpus, so the length of corpus & Eulic is the size of the union set and their difference is the size of intersection 
        Eulic = not_in_corpus
        size_sentence = len(words[i])
        distance.append((len(str) - Eulic)*1.0/(size_sentence + Eulic))
        

    # to get final P
    for i in range(6):
        index = 0
        for j in range(K): 
            index = index + (all_emotion[j][i]/distance[j])
        lable[i] = index
    return lable.index(max(lable))

if __name__=='__main__':
    col_word = data_test['Words']
    words = np.array(col_word)
    words_test = []
    for i in range(len(words)):
        index = words[i].split()
        words_test.append(index)
    N1 = len(words_test)

    emotion_new = []
    
    # to test validation_set

    col_word2 = data_validation['Words']
    words2 = np.array(col_word2)
    words_validation = []     
    for i in range(len(words2)):
        index = words2[i].split()
        words_validation.append(index)
    N2 = len(words_validation)

    _,emotion_validation = get_emotion(data_validation,N2)

    for i in range(N2):#N1
        emotion_new.append(Eucli_distance_KNN(words_test[i]))
    compare_(emotion_validation,emotion_new)
    print(emotion_new)

    # header = ['textid','Words','anger','disgust','fear','joy','sad','surprise']
    # with open('20337268_zhangwenqin_KNN_classification.csv', 'w',newline='') as f:
    #    # 创建writer
    #     writer = csv.writer(f)
    #     writer.writerow(header)
    #     for i in range(len(words)):
    #         writer.writerow(i,[words[i],emotion[emotion_new[i]]])