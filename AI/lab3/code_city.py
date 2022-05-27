from cmath import cos
from email import header
from importlib.resources import path
from json.tool import main
#from os import pread, stat
from re import T
import re
from stat import S_IEXEC
import heapq
class Node:
    def __init__(self,state,pre,cost) -> None:
        self.state = state
        self.pre = pre
        self.cost = cost
edges = [] # 边集
closed = [] # 已经扩展过的结点
frontier = [] #待扩展的结点
path = []
def is_in_frontier(state):
    for f in frontier:
        if state == f[1]:
            return True
    return False

def print_path(result): #打印路径
    while True:
        path.append(result[1])
        if result[2] == None:
            break
        result = result[2]
    path.reverse()

def main():
    m, n = map(int,input().split(" ")) #"Please enter the number of vertex and edge:"
    for _ in range(n):
        n1, n2, w= input().split(" ")
        w = int(w)
        edges.append({'c1':n1, 'c2':n2, 'w':int(w)})

    while True :
        s_city, d_city = input().split(" ")
        ans = uniform_cost_search(s_city, d_city)  
        print('Shortest distance from %s to %s is %d' %(s_city,d_city,ans[0]))
        print_path(ans)
        print('Path:',path) 


def uniform_cost_search(start, dest):
    heapq.heapify(frontier)
    heapq.heappush(frontier,(0,start,None))  # 元组（heapq不支持字典） 分别是 w, state, pre
    
    while len(frontier):
        t = heapq.heappop(frontier)
        if t[1] == dest:  # 目标检测
            return t
        closed.append(t[1])
        for edge in edges:
            des = ''
            if edge['c1'] == t[1]:  # 由于是无向图，当前的城市可以作为边的起点，也可以作为终点
                des = edge['c2']
            elif edge['c2'] == t[1]:
                des = edge['c1']
            if des == '':
                continue
            child = {'state': des, 'pre': t, 'w': t[0]+edge['w']}  # 将子结点封装成一个字典，分别是子结点的状态， 父亲结点， cost
            if child['state'] not in closed:  # 环检测（如果该结点没有被扩展过）
                heapq.heappush(frontier, (child['w'], child['state'], child['pre']))
    return None

if __name__ == '__main__':
    main()

