# -*- coding: utf-8 -*-
# @Time    : 2022/6/2
# @Author  : Ivan-Von
# @FileName: main.py
# @Software: vscode
# @Blog    ：github.com @Ivan-Von
# from read import*
# from deal_data import*
import numpy as np
import pandas as pd
import string
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer

# from nltk.corpus import stopwords
# import nltk
# 如何解决数据集标签不平衡的问题？
# GPU编程提高性能
# 100000 - 112999

# 思路1：TF-IDF + 机器学习分类器
#   直接使用TF-IDF对文本提取特征，并使用分类器进行分类。 在分类器的选择上，可以使用SVM、LR、或者XGBoost。
# 思路2：FastText
#   FastText是入门款的词向量，利用Facebook提供的FastText工具，可以快速构建出分类器。
# 思路3：Word2Vec + 深度学习分类器
#   Word2Vec是进阶款的词向量，并通过构建深度学习分类完成分类。 深度学习分类的网络结构可以选择TextCNN、TextRNN或者BiLSTM。
# 思路4：Bert词向量
#   Bert是高配款的词向量，具有强大的建模学习能力。

train_df = pd.read_csv('lab_final\\train.csv',nrows=100)
sentence_index = train_df['sentence']
sentence = np.array(sentence_index)
# train_df = np.array(train_df)

for i in range(len(sentence)):
    remove = str.maketrans('','',string.punctuation) #去除标点符号
    sentence[i] = sentence[i].translate(remove)

vectorizer = CountVectorizer()
vectorizer.fit_transform(sentence).toarray()
print(vectorizer)

# train_df['text_len'] = train_df['sentence'].apply(lambda x: len(x.split(' ')))
# print(train_df['text_len'].describe())

# _ = plt.hist(len(train_df['sentence']), bins=200)
# plt.xlabel('Text char count')
# plt.title("Histogram of char count")
# plt.savefig('./text_chart_count.png')
# plt.show()


# train_df['gold_label'].value_counts().plot(kind='bar')
# plt.title('News class count')
# plt.xlabel("category")
# plt.savefig('./category.png')
# plt.show()


import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from torch.autograd import Variable
import torch.nn.functional as F

dtype = torch.FloatTensor

# Text-CNN Parameter
embedding_size = 2 # n-gram
sequence_length = 3
num_classes = 2  # 0 or 1
filter_sizes = [2, 2, 2] # n-gram window
num_filters = 3

# 3 words sentences (=sequence_length is 3)
sentences = ["i love you", "he loves me", "she likes baseball", "i hate you", "sorry for that", "this is awful"]
labels = [1, 1, 1, 0, 0, 0]  # 1 is good, 0 is not good.

word_list = " ".join(sentences).split()
word_list = list(set(word_list))
word_dict = {w: i for i, w in enumerate(word_list)}
vocab_size = len(word_dict)

inputs = []
for sen in sentences:
    inputs.append(np.asarray([word_dict[n] for n in sen.split()]))

targets = []
for out in labels:
    targets.append(out) # To using Torch Softmax Loss function

input_batch = Variable(torch.LongTensor(inputs))
target_batch = Variable(torch.LongTensor(targets))


class TextCNN(nn.Module):
    def __init__(self):
        super(TextCNN, self).__init__()

        self.num_filters_total = num_filters * len(filter_sizes)
        self.W = nn.Parameter(torch.empty(vocab_size, embedding_size).uniform_(-1, 1)).type(dtype)
        self.Weight = nn.Parameter(torch.empty(self.num_filters_total, num_classes).uniform_(-1, 1)).type(dtype)
        self.Bias = nn.Parameter(0.1 * torch.ones([num_classes])).type(dtype)

    def forward(self, X):
        embedded_chars = self.W[X] # [batch_size, sequence_length, sequence_length]
        embedded_chars = embedded_chars.unsqueeze(1) # add channel(=1) [batch, channel(=1), sequence_length, embedding_size]

        pooled_outputs = []
        for filter_size in filter_sizes:
            # conv : [input_channel(=1), output_channel(=3), (filter_height, filter_width), bias_option]
            conv = nn.Conv2d(1, num_filters, (filter_size, embedding_size), bias=True)(embedded_chars)
            h = F.relu(conv)
            # mp : ((filter_height, filter_width))
            mp = nn.MaxPool2d((sequence_length - filter_size + 1, 1))
            # pooled : [batch_size(=6), output_height(=1), output_width(=1), output_channel(=3)]
            pooled = mp(h).permute(0, 3, 2, 1)
            pooled_outputs.append(pooled)

        h_pool = torch.cat(pooled_outputs, len(filter_sizes)) # [batch_size(=6), output_height(=1), output_width(=1), output_channel(=3) * 3]
        h_pool_flat = torch.reshape(h_pool, [-1, self.num_filters_total]) # [batch_size(=6), output_height * output_width * (output_channel * 3)]

        model = torch.mm(h_pool_flat, self.Weight) + self.Bias # [batch_size, num_classes]
        return model

model = TextCNN()

criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Training
for epoch in range(5000):
    optimizer.zero_grad()
    output = model(input_batch)

    # output : [batch_size, num_classes], target_batch : [batch_size] (LongTensor, not one-hot)
    loss = criterion(output, target_batch)
    if (epoch + 1) % 1000 == 0:
        print('Epoch:', '%04d' % (epoch + 1), 'cost =', '{:.6f}'.format(loss))

    loss.backward()
    optimizer.step()

# Test
test_text = 'sorry hate you'
tests = [np.asarray([word_dict[n] for n in test_text.split()])]
test_batch = Variable(torch.LongTensor(tests))

# Predict
predict = model(test_batch).data.max(1, keepdim=True)[1]
if predict[0][0] == 0:
    print(test_text, "is Bad Mean...")
else:
    print(test_text, "is Good Mean!!")
