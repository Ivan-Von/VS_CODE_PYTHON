# -*- coding: utf-8 -*-
# @Time    : 2019/4/11
# @Author  : Zhao huilin
# @FileName: dijkstra.py
# @Software: PyCharm
# @Blog    ：https://me.csdn.net/nominior
import numpy as np
 
graph_chain = {
    'a': {'b': 7, 'c': 9, 'f': 14},
    'b': {'a': 7, 'c': 10, 'd': 15},
    'c': {'a': 9, 'b': 10, 'd': 11, 'f': 2},
    'd': {'b': 15,'c': 11, 'e': 6},
    'e': {'d': 6, 'f': 9},
    'f': {'a': 14, 'c': 2, 'e': 9}
}
# 这里矩阵未传入graph中使用，而是在graph使用链表生成，也可以传入矩阵和及按顺序的点列表
# 但矩阵在后续处理中是必须的，应为此代码后续处理基于矩阵进行权重查找
graph_matrix = [[0.0, 7.0, 9.0, np.inf, np.inf, 14.0],
                 [7.0, 0.0, 10.0, 15.0, np.inf, np.inf], 
                 [9.0, 10.0, 0.0, 11.0, np.inf, 2.0], 
                 [np.inf, 15.0, 11.0, 0.0, 6.0, np.inf], 
                 [np.inf, np.inf, np.inf, 6.0, 0.0, 9.0], 
                 [14.0, np.inf, 2.0, np.inf, 9.0, 0.0]]
 
 
class graph():
    def __init__(self,vertexs=None,chain=None,matrix=None):
        self.vertexs = vertexs
        self.chain = chain
        self.matrix = matrix
        if vertexs is None and chain is not None:
            self.vertexs = list(chain.keys())
        if matrix is None and chain is not None:
            self.matrix = self.chain_matrix()
 
    def __str__(self):
        return str(self.chain)
 
    def chain_matrix(self):
        matrix = np.zeros((len(self.vertexs), len(self.vertexs)))
        matrix += np.inf
        keys = list(self.chain.keys())
        for key, value in self.chain.items():
            key_index = self.vertexs.index(key)
            for k, v in value.items():
                k_index = self.vertexs.index(k)
                matrix[key_index][k_index] = v
            matrix[key_index][key_index] = 0
        return matrix.tolist()
 
 
class dijkstra_path():
    def __init__(self,graph,src_vertex):
        self.graph = graph
        self.src_vertex = src_vertex
        self.set = self.get_set()
        self.unsearch = self.get_unsearch()
        self.dis = self.get_dis()
        self.path = self.get_path()
        self.point = self.get_point()
 
 
    def get_set(self):
        return [self.src_vertex]
    def get_unsearch(self):
        unsearch = self.graph.vertexs[:]
        unsearch.remove(self.src_vertex)
        return unsearch
    def get_dis(self):
        dis = {}
        vertexs = self.graph.vertexs
        index = vertexs.index(self.src_vertex)
        for i,distance in enumerate(self.graph.matrix[index]):
            dis[vertexs[i]] = distance
        return dis
    def get_path(self):
        path = {}
        vertexs = self.graph.vertexs
        index = vertexs.index(self.src_vertex)
        for i,distance in enumerate(self.graph.matrix[index]):
            path[vertexs[i]] = []
            if distance != np.inf:
                path[vertexs[i]].append(self.src_vertex)
        return path
 
    def get_point(self):
        return self.src_vertex
 
    # 首先根据dis、index及set(若出现权重相等)确定下一个路径点
    def update_point(self,index):
        dis_sort = list(self.dis.values())
        dis_sort.sort()
        point_dis = dis_sort[index]
        for key,distance in self.dis.items():
            if distance == point_dis and key not in self.set:
                self.point = key
                break
     # 路径、距离更新，原距离>point距离+point到各点距离，则更新
    def update_dis_path(self):
        new_dis = {}
        index_point = self.graph.vertexs.index(self.point)
        for i,key in enumerate(self.dis.keys()):
            new_dis[key] = self.dis[self.point] + self.graph.matrix[index_point][i]
            if new_dis[key]<self.dis[key]:
                self.dis[key] = new_dis[key]
                # self.path[key] = self.path[self.point].append(self.point)
                self.path[key] =self.path[self.point].copy()
                self.path[key].append(self.point)
 
 
    def find_shortestPath(self,dst_vertex=None,info_show=False):
        count = 1
        if info_show:
            print('*' * 10, 'initialize', '*' * 10)
            self.show()
        while self.unsearch:
            self.update_point(count)
            self.set.append(self.point)
            self.unsearch.remove(self.point)
            self.update_dis_path()
            if info_show:
                print('*' * 10, 'produce', count, '*' * 10)
                self.show()
            count+=1
            if dst_vertex != None and dst_vertex in self.set:
                result = self.path[dst_vertex].copy()
                result.append(dst_vertex)
                return result
        return self.path
 
 
 
    def show(self):
        print('set:',self.set)
        print('unsearch:',self.unsearch)
        print('point:',self.point)
        print('dis:',self.dis.values())
        print('path:',self.path.values())
 
 
if __name__ == '__main__':
    gp = graph(chain=graph_chain)
 
    dp = dijkstra_path(gp,'e')
    result = dp.find_shortestPath('a')
    print(result)
 
 