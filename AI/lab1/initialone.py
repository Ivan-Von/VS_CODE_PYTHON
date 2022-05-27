import time
max = 99999
    #定义初始数
with open('Romania.txt')as file_object:
    m,n = file_object.readline().split()
    m = int(m)
    n = int(n)
    #返回一个新集合
    #[(m,n)]是初始输入的节点数和边数
nodes = [] 
    #创建列表存储所有的点
dic = {} 
    #创建字典存储点和对应的数字，将字典中点转化为数字共存
count = 0
    #计数器
matrix = [[99999 for i in range(m)] for i in range(m)] 
    #创建邻接矩阵
for i in range(m):
    matrix[i][i] = 0
    #初始化邻接矩阵

    #构造邻接矩阵
node_1 = node_2 = None
value = 0
with open('Romania.txt')as file_object:
    for i in range(n + 1):
        if i == 0:
            line = file_object.readline()
            continue
        else:
            node_1,node_2,value = file_object.readline().split()
    # value = int(value)
            #不一定是数字，先进行转化
        if(node_1 not in nodes):
            #1. 存入新的点 2. 把点转化为数字对应 3. 计数器递增
            nodes.append(node_1)
            dic[node_1] = count
            count+=1
        if(node_2 not in nodes):
            nodes.append(node_2)
            dic[node_2] = count
            count+=1
        #因为数字做索引，所以要把字母的节点名称转化为数字的节点
        #考虑过asii码对应，也可以
        matrix[dic[node_1]][dic[node_2]] = value
        matrix[dic[node_2]][dic[node_1]] = value

a,b = input().split()
    #输入要进行计算的点
state = [0 for i in range(m)]
    # 0 则该点未找出最短路径， 1 则该点已找出最短路径
length = [99999 for i in range(m)]
    # 从源点到其他点的最短路径大小
pre_able = [a for i in range(m)]
    #该点到初始点的最短路径的上前驱点，可达点
for node in nodes:
    length[dic[node]] = matrix[dic[a]][dic[node]]
#最短路径初始化为其他点到它的距离，直到所有点都遍历完，结束循环
while 0 in state:
    #找到未遍历的点中，与已遍历的点距离最近的那一个
    node = a
    dis = 99999 #比较距离
    for node1 in nodes: #nodes是所有点 
        if state[dic[node1]] == 0 and length[dic[node1]] < dis:#?
            dis = length[dic[node1]]
            node = node1
    #找到可达点able进行更新
    #将此点标记，并更新其它未遍历点的length与able
    state[dic[node]] = 1
    for node2 in nodes: #nodes是所有点
        if state[dic[node2]] == 0 and length[dic[node]] + matrix[dic[node2]][dic[node]] < length[dic[node2]]:
            length[dic[node2]] = length[dic[node]] + matrix[dic[node2]][dic[node]]
            pre_able[dic[node2]] = node
    #更新able在最短路径上的点
shortest_path = []
#short_path记录点a到点b的最短路径
node_back = b
#这里写k = None会报错，为什么？
while node_back != a:
    shortest_path.append(node_back)
    node_back = pre_able[dic[node_back]]
shortest_path.append(a)

#输出最短路径
index = len(shortest_path)
print('shortest_path:\t',end = '')
while index:
    print(shortest_path.pop(),end = '\t\t')
    index = index - 1
print('')
#输出最短路径长度
print('length: ',length[dic[b]])
filename = 'diary.txt'
with open(filename,'a') as file_object:
    file_object.write(time.strftime("%Y-%m-%d %H:%M:%S : from\t",time.localtime()))
    file_object.write(a)
    file_object.write('\tto\t')
    file_object.write(b)
    file_object.write('\n')