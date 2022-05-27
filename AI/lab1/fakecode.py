from dis import dis
from itertools import count

from numpy import append


max  = 99999
m,n = input()
#读入节点数和边数
nodes = []
#定义点的数组
dic = {}
#定义点和数字的对应关系
matrix = [m][n] = 0 
#初始化
node_1,node_2,value = input()
#左边、右边、权值

#建造邻接矩阵
for i in range(n):
#对n个点都进行对应，下述代码1换成2，2换成1并列选择执行
    if(node_1 not in nodes):
        nodes.append(node_1)
        dic[node_1] = count
        count += 1
    matrix[dic[node_1]][dic[node_2]] = value

a,b = input().split()
#读入待解决的点
state[n] = 0
#是否已经找到最短路径
length[m] = matrix[dic[a]][dic[[node]]
#初始化
pre_able[m] = a
#前驱点，方便找到路径
while 0 in state:
    for node1 in nodes:
        #第一次先找到可达最短点
        if state[dic[node1]] == 0 && length[dic[node1]] < dis:
            dis = length[dic[node1]]
            node = node1
    state[dic[node]] = 1
    for node2 in nodes:
        #核心算法，进行更新
        if state[dic[node2]] == 0 &&length[dic[node]] + matrix[dic[node2]][dic[node]] < length[dic[node2]]:
            length[dic[node2]] = length[dic[node]] + matrix[dic[node2]][dic[node]]
            pre_able[dic[node2]] = node
shortest_path = []
#存储路径的数组
node_back = b
#存储下一个节点
while node_back != a:
    shortest_path.append(node_back)
    node_back = pre_able[dic[node_back]]
shortest_path.append(a)

print(path,shortest_path)