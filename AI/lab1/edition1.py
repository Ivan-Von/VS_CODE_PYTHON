import Function
import time
import City
max = 99999
#get m,n
with open('Romania.txt')as file_object:
    m,n = file_object.readline().split()
    m = int(m)
    n = int(n)
nodes = [] 
dic = {} 
count = 0
matrix = [[max for i in range(m)] for i in range(m)] 
for i in range(m):
    matrix[i][i] = 0
node_1 = node_2 = None
value = 0
Function.__get_matrix__(n,matrix,nodes,dic,count)
#get a,b
a,b = input().split()
for i in range(m):
    if a == nodes[i] or a == nodes[i][0].upper() or a == nodes[i].upper() or a == nodes[i].lower() or a == nodes[i][0].lower():
        a = nodes[i]
    if b == nodes[i] or b == nodes[i][0].upper() or b == nodes[i].upper() or b == nodes[i].lower() or b == nodes[i][0].lower():
        b = nodes[i]
state = [0 for i in range(m)]
length = [99999 for i in range(m)]
pre_able = [a for i in range(m)]
shortest_path = []
Function.__Body__(a,b,matrix,dic,nodes,state,length,pre_able,shortest_path)
index = len(shortest_path)
Function.__print_path__(shortest_path,length[dic[b]],index)
distance = str(length[dic[b]])
Function.__Diary__(a,b,distance)