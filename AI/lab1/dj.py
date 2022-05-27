# -*- coding:utf-8 -*-
from math import radians

#求解各节点最短路径，获取path，和cost数组， 
#path[i] 表示vi节点的前继节点索引，一直追溯到起点。 
#cost[i] 表示vi节点的花费 

def dijkstra(graph, startIndex, path, cost, max):
    lenth =  len(graph)
    v = [0] * lenth
    #初始化path,cpst,V
    for i in range(lenth):
        if i == startIndex:
            v[startIndex] = 1
        else:
            cost[i] = graph[startIndex][i] 
            path[i] = (startIndex if(cost[i] < max) else -1)
    #print v, cost, path
    for i in range(1, lenth):
        minCost = max
        curNode = -1
    for w in range(lenth):
        if v[w] == 0 and cost[w] < minCost:
            minCost = cost[w]
            curNode = w
    #获取最小权值的节点
        if curNode == -1:break #python没有括号，注意缩进
        v[curNode] = 1
    for w in range(lenth):#更新节点
        if v[w] == 0 and(graph[curNode][w] + cost[curNode] < cost[w]):
            cost[w] = graph[curNode][w] + cost[curNode]
            path[w] = curNode
    return path

if __name__ == '_main_':
    max = 2147483647
    graph = [
        [max,max,10,max,30,100],
        [max, max, 5, max, max, max],
        [max, max, max, 50, max, max],
        [max, max, max, max, max, 10],
        [max, max, max, 20, max, 60], 
        [max, max, max, max, max, max]
    ]
    path = [0]*6
    cost = [0] * 6
    print (dijkstra(graph, 0, path,cost,max))