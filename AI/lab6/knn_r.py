import numpy as np
def distance(v1, v2, dis_type):
    if dis_type == 1:
        return np.sum(np.abs(v1 - v2))  # 哈夫曼距离
    elif dis_type == 2:
        return np.sqrt(np.sum(np.square(v1 - v2)))  # 欧式距离
    elif dis_type == 3:  # 自定义距离
        vsum = v1 + v2
        cnt0 = len(np.where(vsum == 0)[0])  # 两个向量相同位置都是0的个数
        cnt1 = len(np.where(vsum == 1)[0])  # 两个向量相同位置一个是0一个是1的个数
        cnt2 = len(np.where(vsum == 2)[0])  # 两个向量相同位置都是1的个数
        res = cnt1 * 8 + cnt0 - cnt2 * 24
        return 0 if res < 0 else res

def knn_reg_select(one_hot, vector_in, k):
    """
    :param one_hot: 训练集语料构成的onehot矩阵
    :param vector_in: 要预测的语句所转变成的onehot向量
    :param k: knn算法中的参数k
    :return: 预测的标签可能性列表
    """
    dis2indexs = []
    for row, one_hot_line in enumerate(one_hot):  # 计算vector_in与训练集onehot的距离，放入一个list
        dis = distance(one_hot_line, vector_in, 3)
        dis2indexs.append(dis2index(dis, row))
    emotion_probabilities = [0] * 6
    dis2indexs.sort()  # 对距离（附加索引）排序
    for i in range(k):  # 取出前k个距离最小的
        mind = dis2indexs[i]
        # 将距离的倒数作为权值，乘以训练集中的概率，加和得到总概率（注：处理了一下分母0的情况）
        for k, p in enumerate(emotions_train_regression[mind.index]):
            emotion_probabilities[k] += 999999 if mind.dis == 0 else p / (mind.dis**55)
    p_sum = sum(emotion_probabilities)
    if p_sum > 0:
        emotion_probabilities = [p / p_sum for p in emotion_probabilities]  # 对概率归一化处理
    return emotion_probabilities