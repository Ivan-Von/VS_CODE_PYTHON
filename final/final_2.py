# -*- coding: utf-8 -*-
from asyncore import write
import string
import nltk
import sklearn
import itertools as it
import numpy as np
import pandas as pd
from copy import deepcopy
from gensim.models import word2vec
from nltk.corpus import stopwords
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
'''
#处理数据，包括数据清洗、数据切割、单词向量化、文本数据向量化，并保存结果
dataset = pd.read_csv("train.csv",header=0)#读取数据
dataset = np.array(dataset)
for data in dataset:    #对数据集进行处理，把大写转为小写以及去除标点符号
    data2 = data[2]
    data2 = data2.lower()
    remove = str.maketrans('','',string.punctuation) 
    data2 = data2.translate(remove)

    # data2 = nltk.word_tokenize(data2)#分词
    # data2 = [da for da in data2 if not da in stopwords.words('english')]#去除停用词
    # s = nltk.stem.SnowballStemmer('english')#词干化
    # data2 = [s.stem(da) for da in data2]

    data[2] = data2 #用处理好的数据替换原数据
trainset = []
proveset = []
length = len(dataset)
length8 = 0.8*length    #提取数据集的样本按二八分割成测试集和训练集
for i in range(length):
    if i < length8:
        trainset.append(dataset[i][2])
    else :
        proveset.append(dataset[i][2])
#保存清洗分割后的数据集
pd.DataFrame(trainset).to_csv("trainset.csv",header=None,index=None)
pd.DataFrame(proveset).to_csv("proveset.csv",header=None,index=None)
pd.DataFrame(dataset).to_csv("dataset.csv",header=None,index=None)
'''

""" 
#把总样本和对应的标签按照二八比例随机划分为测试集和训练集
dataset = pd.read_csv("dataset.csv",header=None)
dataset = np.array(dataset)
X = dataset[:,2]
Y = dataset[:,1]
X_train,X_test,y_train,y_test = train_test_split(X,Y,test_size=0.2,random_state=1)
"""

""" 
X_tr = np.array(X_train)
pd.DataFrame(X_tr).to_csv("X_tr.csv",header=None,index=None)
#使用训练集来生成二百维的词向量(word2vec方法)
sentences = word2vec.Text8Corpus('X_tr.csv')
model = word2vec.Word2Vec(sentences, sg=1, vector_size=200,  window=6,  min_count=5,  negative=10, sample=0.001, hs=1, workers=4)  # 生成词向量空间模型
model.save('X_tr_word2vec.model') 
"""

""" 
model = word2vec.Word2Vec.load('X_tr_word2vec.model')  #加载模型1
xtr_vec = []
ytr_vec = []
for i in range(len(X_train)):
    ss = X_train[i].split()
    tmp = []
    for s in ss:
        if model.wv.__contains__(s):
            tmp.append(model.wv[s])
    if len(tmp) > 5:
        tmp = np.array(tmp)
        tmp = tmp.transpose()
        pca = PCA(n_components=5)
        tmp = pca.fit_transform(tmp)
        tmp = np.array(tmp)
        tmp = tmp.transpose()
        xtr_vec.append(list(it.chain(*tmp)))
        ytr_vec.append(y_train[i])
pd.DataFrame(xtr_vec).to_csv("XXtr_vec.csv",header=None,index=None)
pd.DataFrame(ytr_vec).to_csv("YYtr_vec.csv",header=None,index=None)

xte_vec = []
yte_vec = []
for i in range(len(X_test)):
    ss = X_test[i].split()
    tmp = []
    for s in ss:
        if model.wv.__contains__(s):
            tmp.append(model.wv[s])
    if len(tmp) > 5:
        tmp = np.array(tmp)
        tmp = tmp.transpose()
        pca = PCA(n_components=5)
        tmp = pca.fit_transform(tmp)
        tmp = np.array(tmp)
        tmp = tmp.transpose()
        xte_vec.append(list(it.chain(*tmp)))
        yte_vec.append(y_test[i])
pd.DataFrame(xte_vec).to_csv("XXte_vec.csv",header=None,index=None)
pd.DataFrame(yte_vec).to_csv("YYte_vec.csv",header=None,index=None)
""" 

'''
#使用整个数据集来生成二百维的词向量(word2vec方法)
train = pd.read_csv("trainset.csv",header=None)
train = np.array(train)
test = pd.read_csv("proveset.csv",header=None)
test = np.array(test)
total = np.vstack((train,test))
pd.DataFrame(total).to_csv("total.csv",header=None,index=None)
sentences = word2vec.Text8Corpus('total.csv')
model = word2vec.Word2Vec(sentences, sg=1, vector_size=200,  window=6,  min_count=5,  negative=10, sample=0.001, hs=1, workers=4)  # 生成词向量空间模型
model.save('total_word2vec.model')
'''

""" 
model = word2vec.Word2Vec.load('total_word2vec.model') #加载模型2
#把每个样本的单词转化为对应的词向量,把不足五个词的样本从数据集中剔除,多余五个词的则对词向量进行PCA降维,
#使训练样本中的每一个都有且仅有五个词向量，然后把五个词向量拼接成一个一千维的向量，即是该样本对应的向量表示
#最后把得到的训练样本、测试样本及其标签分别保存起来
xtr_vec = []
ytr_vec = []
for i in range(len(X_train)):
    ss = X_train[i].split()
    tmp = []
    for s in ss:
        if model.wv.__contains__(s):
            tmp.append(model.wv[s])
    if len(tmp) > 5:
        tmp = np.array(tmp)
        tmp = tmp.transpose()
        pca = PCA(n_components=5)
        tmp = pca.fit_transform(tmp)
        tmp = np.array(tmp)
        tmp = tmp.transpose()
        xtr_vec.append(list(it.chain(*tmp)))
        ytr_vec.append(y_train[i])
pd.DataFrame(xtr_vec).to_csv("xtr_vec.csv",header=None,index=None)
pd.DataFrame(ytr_vec).to_csv("ytr_vec.csv",header=None,index=None)

xte_vec = []
yte_vec = []
for i in range(len(X_test)):
    ss = X_test[i].split()
    tmp = []
    for s in ss:
        if model.wv.__contains__(s):
            tmp.append(model.wv[s])
    if len(tmp) > 5:
        tmp = np.array(tmp)
        tmp = tmp.transpose()
        pca = PCA(n_components=5)
        tmp = pca.fit_transform(tmp)
        tmp = np.array(tmp)
        tmp = tmp.transpose()
        xte_vec.append(list(it.chain(*tmp)))
        yte_vec.append(y_test[i])
pd.DataFrame(xte_vec).to_csv("xte_vec.csv",header=None,index=None)
pd.DataFrame(yte_vec).to_csv("yte_vec.csv",header=None,index=None) 
"""

""" 
#加载训练样本和测试样本及其标签(词向量建立在训练集上)
xtr_vec = pd.read_csv("xtr_vec.csv")
xtr_vec = np.array(xtr_vec)
ytr_vec = pd.read_csv("ytr_vec.csv")
ytr_vec = np.array(ytr_vec)
xte_vec = pd.read_csv("xte_vec.csv")
xte_vec = np.array(xte_vec)
yte_vec = pd.read_csv("yte_vec.csv")
yte_vec = np.array(yte_vec)
"""

""" 
#加载训练样本和测试样本及其标签(词向量建立在总数据集上)
xtr_vec = pd.read_csv("XXtr_vec.csv")
xtr_vec = np.array(xtr_vec)
ytr_vec = pd.read_csv("YYtr_vec.csv")
ytr_vec = np.array(ytr_vec)
xte_vec = pd.read_csv("XXte_vec.csv")
xte_vec = np.array(xte_vec)
yte_vec = pd.read_csv("YYte_vec.csv")
yte_vec = np.array(yte_vec) """


""" #得到训练集中的正标签和负标签的比例作为另一方的权重用来进行逻辑回归
count0 = 0
count1 = 0
for y in ytr_vec:
    if y == 0:
        count0 += 1
    if y == 1:
        count1 += 1
#print(count0,count1,len(ytr_vec))
weight0 = np.float32(count0/len(ytr_vec))
weight1 = np.float32(count1/len(ytr_vec))
#print(weight0,weight1)
model = LogisticRegression(penalty="l2",solver="liblinear",C=0.8,max_iter=1000,class_weight={1:weight0,0:weight1})#建立模型
ytr_vec = ytr_vec.ravel()
model.fit(xtr_vec,ytr_vec)#训练 """

""" 
#这一段是取所有的负测试样例或者正测试样例进行预测，分别看预测结果
xtmp = []
ytmp = []
for i in range(len(xte_vec)):
    if yte_vec[i] == 0:
        xtmp.append(xte_vec[i])
        ytmp.append(yte_vec[i])
xtmp = np.array(xtmp)
ytmp = (np.array(ytmp)).ravel() 
ypre = model.predict(xtmp)
count = 0
for i in range(len(ytmp)):
    if ytmp[i] == ypre[i]:
        count += 1
print("The number of the test datas is",len(ytmp),",and the number of the correct is",count,",so the correct rate is",np.float64(count/len(ytmp)))
"""

""" 
#取测试集中的某一个子集
xte_vec = xte_vec[2500:2595,:]
yte_vec = yte_vec[2500:2595,:]
"""

""" #对测试集进行测试
yte_vec = yte_vec.ravel()
ypre = model.predict(xte_vec)
#print(sklearn.metrics.f1_score(yte_vec, ypre, average='weighted', sample_weight=None))

#计算F1-score值
TP = 0
TN = 0
FP = 0
FN = 0
for i in range(len(ypre)):
    if yte_vec[i] == 0 and ypre[i] == 0:
        TN += 1
    if yte_vec[i] == 1 and ypre[i] == 0:
        FN += 1
    if yte_vec[i] == 0 and ypre[i] == 1:
        FP += 1
    if yte_vec[i] == 1 and ypre[i] == 1:
        TP += 1 
Acc = np.float32((TN+TP)/(len(ypre)))
rec = np.float32(TP/(TP+FN))
f1s = np.float64(2*((Acc*rec)/(Acc+rec)))
print("TP:",TP,"FN:",FN,"TN:",TN,"FP:",FP)
print("Acc:",Acc,"rec:",rec)
print("F1-score is",f1s) """

""" 
#计算正确率
count = 0
for i in range(len(yte_vec)):
    if yte_vec[i] == ypre[i]:
        count += 1
print("The number of the test datas is",len(yte_vec),",and the number of the correct is",count,",so the correct rate is",np.float64(count/len(yte_vec))) 
"""


import csv
xtr_vec = pd.read_csv("final\\xtr_vec.csv")
xtr_vec = np.array(xtr_vec)
ytr_vec = pd.read_csv("final\\ytr_vec.csv")
ytr_vec = np.array(ytr_vec)
xte_vec = pd.read_csv("final\\xte_vec.csv")
xte_vec = np.array(xte_vec)
yte_vec = pd.read_csv("final\\yte_vec.csv")
yte_vec = np.array(yte_vec)
xx = np.vstack((xtr_vec,xte_vec))
yy = np.vstack((ytr_vec,yte_vec))
#得到训练集中的正标签和负标签的比例作为另一方的权重用来进行逻辑回归
count0 = 0
count1 = 0
for y in yy:
    if y == 0:
        count0 += 1
    if y == 1:
        count1 += 1
#print(count0,count1,len(yy))
weight0 = np.float32(count0/len(yy))
weight1 = np.float32(count1/len(yy))
#print(weight0,weight1)
models = LogisticRegression(penalty="l2",solver="liblinear",C=0.8,max_iter=1000,class_weight={1:weight0,0:weight1})#建立模型
yy = yy.ravel()
models.fit(xx,yy)#训练
datas = pd.read_csv("final\\test_new.csv")
datas = np.array(datas)
data = deepcopy(datas)

# with open('data.csv','w',newline='',encoding='utf-8')as f:
#     writer = csv.writer(f)
for da in data:    #对数据集进行处理，把大写转为小写以及去除标点符号
    da2 = da[1]
    da2 = da2.lower()
    remove = str.maketrans('','',string.punctuation) 
    da2 = da2.translate(remove)
    da[1] = da2
        #writer.writerow([da2])
model = word2vec.Word2Vec.load('final\\total_word2vec.model')
xte = data[:,1]
x = []
for i in range(len(xte)):
    ss = xte[i].split()
    tmp = []
    for s in ss:
        if model.wv.__contains__(s):
            tmp.append(model.wv[s])
    if len(tmp) > 5:
        tmp = np.array(tmp)
        tmp = tmp.transpose()
        pca = PCA(n_components=5)
        tmp = pca.fit_transform(tmp)
        tmp = np.array(tmp)
        tmp = tmp.transpose()
    if len(tmp) < 5:
        n = 0
        for t in tmp:
            s = model.wv.most_similar(t,topn=1)[0][0]
            ve = model.wv.most_similar(t,topn=1)[0][1]
            if n < ve:
                n = ve
                ss = s
        for j in range(5-len(tmp)):
            tmp.append(model.wv[ss])
    x.append(list(it.chain(*tmp)))
ypr = models.predict(x)
ypr[:, np.newaxis]
for i in range(len(datas)):
    datas[i][1] = ypr[i]
pd.DataFrame(datas).to_csv('20337268_zhangwenqin.csv',header=['sentenceID','gold_label'],index=None)