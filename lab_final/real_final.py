# -*- coding: utf-8 -*- #

# ------------------------------------------------------------------
# File Name:        final.py
# Author:           git@github.com:Ivan-Von.git
#                   @Adria_Von
# Version:          ver_01
# Created:          2022/6/10
# Description:      Main Function: 解决反事实陈述语句判断问题
# Function List:    
# History:
#       <author>        <version>       <time>      <con>
#       @Adria          ver01           2022/6/10   framework
#       @Adria          vec02           2022/6/12   CNN
#       @Adria          vec03           2022/6/13   finish
# ------------------------------------------------------------------


from cProfile import label
import numpy as np
import csv
import pandas as pd
import torch
import torch.nn as nn
import torch.optim as optim
from torch.autograd import Variable
import torch.nn.functional as F
from torch.nn.utils.rnn import pad_sequence
import string
dtype = torch.FloatTensor

# Text-CNN Parameter
embedding_size = 2 # n-gram
sequence_length = 3
num_classes = 2  # 0 or 1
filter_sizes = [2, 2, 2] # n-gram window
num_filters = 3
# train data file
train_df = pd.read_csv('lab_final\\train.csv',nrows=1000)
test_df = pd.read_csv('lab_final\\test.csv',nrows=100)
test_sentence_index = test_df['sentence']
test_sentence = np.array(test_sentence_index)

for i in range(len(test_sentence)):
    remove = str.maketrans('','',string.punctuation) #去除标点符号
    test_sentence[i] = test_sentence[i].translate(remove)

sentence_index = train_df['sentence']
sentences = np.array(sentence_index)


for i in range(len(sentences)):
    remove = str.maketrans('','',string.punctuation) #去除标点符号
    sentences[i] = sentences[i].translate(remove)


labels = train_df['gold_label']
answer_label = test_df['gold_label']
answer_label = np.array(answer_label)
labels = np.array(labels)
index = []
for i in range(len(sentences)):
    index.append(sentences[i])
for i in range(len(test_sentence)):
    index.append(test_sentence[i])


word_list = " ".join(index).split()
word_list = list(set(word_list))
word_dict = {w: i for i, w in enumerate(word_list)}
vocab_size = len(word_dict)

inputs = []
for sen in sentences:
    inputs.append(np.asarray([word_dict[n] for n in sen.split()]))

split_to_ori = pad_sequence([torch.tensor(dim) for dim in inputs], batch_first=True)

targets = []
for out in labels:
    targets.append(out) # To using Torch Softmax Loss function
    
#input_batch = Variable(torch.LongTensor(inputs))
input_batch = split_to_ori
target_batch = Variable(torch.LongTensor(targets))
# print(len(input_batch))
# print(len(target_batch))

class CNN(nn.Module):
    def __init__(self):
        super(CNN, self).__init__()

        self.num_filters_total = num_filters * len(filter_sizes)
        self.W = nn.Parameter(torch.empty(vocab_size, embedding_size).uniform_(-1, 1)).type(dtype)
        self.Weight = nn.Parameter(torch.empty(self.num_filters_total, num_classes).uniform_(-1, 1)).type(dtype)
        self.Bias = nn.Parameter(0.1 * torch.ones([num_classes])).type(dtype)

    def forward(self, X):
        X = X.type(torch.long)
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

model = CNN()

criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Training
for epoch in range(5000):
    optimizer.zero_grad()
    # 这里开始output的大小改变了
    output = model(input_batch)

    # output : [batch_size, num_classes], target_batch : [batch_size] (LongTensor, not one-hot)
    # loss = criterion(output, target_batch)

    # loss.backward()
    optimizer.step()

answer = []
header = ['textid','Words','label']
with open('cnn.csv', 'w',newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for i in range(len(test_sentence)):
        # Test
        test_text = test_sentence[i]
        remove = str.maketrans('','',string.punctuation) #去除标点符号
        test_text = test_text.translate(remove)
        tests = [np.asarray([word_dict[n] for n in test_text.split()])]# key error
        test_batch = Variable(torch.LongTensor(tests))
        # Predict
        predict = model(test_batch).data.max(1, keepdim=True)[1]
        if predict[0][0] == 0:
            writer.writerow([i,test_text,'0'])
            answer.append(1)
            # writer.writerow(i,[words[i],emotion[emotion_new[i]]])
            print(test_text, "is Bad Mean...")
        else:
            writer.writerow([i,test_text,'1'])
            answer.append(0)
            print(test_text, "is Good Mean!!")
    # 创建writer
true_answer = 0
for i in range(len(answer_label)):
    if answer_label[i] == answer[i]:
        true_answer +=1
print(true_answer*1.0/len(answer))