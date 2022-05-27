def knn_cla_select(one_hot, vector_in, k):
    """
    :param one_hot: 训练集语料构成的onehot矩阵
    :param vector_in: 要预测的语句所转变成的onehot向量
    :param k: knn算法中的参数k
    :return: 预测的标签
    """
    dis2indexs = []
    for row, one_hot_line in enumerate(one_hot):  # 计算vector_in与训练集onehot的距离，放入一个list
        dis = distance(one_hot_line, vector_in, 2)
        dis2indexs.append(dis2index(dis, row))
    emotions_cnt = {}
    max_cnt = 0
    select_emotion = ""
    dis2indexs.sort()  # 对距离（附加索引）排序，python使用的是归并排序，因此是稳定的排序
    for i in range(k):  # 取出前k个距离最小的
        mind = dis2indexs[i]
        emot = emotions_train[mind.index]
        #  对于这k个最小的距离对应的标签，出现n次就加上权值*n，这里的权值取的是 1÷(距离^5)
        weight = float("inf") if mind.dis == 0 else 1 / (mind.dis ** 5)
        if emotions_cnt.get(emot, -1) == -1:
            emotions_cnt[emot] = weight
        else:
            emotions_cnt[emot] += weight
        if emotions_cnt[emot] > max_cnt:  # 记录k个中标签次数出现最多的标签，作为最后的输出
            select_emotion = emot
            max_cnt = emotions_cnt[emot]
    return select_emotion