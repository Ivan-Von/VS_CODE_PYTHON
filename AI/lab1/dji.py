import time
MAX = 99999

class City():
    def __init__(self,name):
        self.name = name
    name = str         

with open('Romania.txt')as file_object:
    m,n = file_object.readline().split()
    m = int(m)
    n = int(n)
print(m,n)
#'str' object cannot be interpreted as an integer

#nodes = [City for i in range(m)]
nodes = []
dic = {}
count = 0
matrix = [[MAX for i in range(m)]for i in range(m)]
for i in range(m):
    matrix[i][i] = 0
node_1 = node_2 = City
value1 = None
i = 0
for i in range(n+1):
    with open('Romania.txt')as file_object:
        if i == 1:
            line = file_object.readline()
            print(line)
        else:
            #node_1.name,node_2.name,value1 = file_object.readline().split()
        #not enough values to unpack (expected 3, got 2)
            line = file_object.readline()
            print(line)
    value = int(value1)
    if(node_1 not in nodes):
        nodes.append(node_1)
        dic[node_1.name] = count
        count += 1
    if(node_2 not in nodes):
        nodes.append(node_2)
        dic[node_2.name] = count
        count += 1
    matrix[dic[node_1.name]][dic[node_2.name]] = value
    matrix[dic[node_2.name]][dic[node_1.name]] = value
    
    #matrix[dic[node_1]][dic[node_2]] = value
    #matrix[dic[node_2]][dic[node_1]] = value
    #'Sibiu'

a = b = City
a.name,b.name = input().split()
for i in range(m):
    if a.name == nodes[i].name or a.name == nodes[i].name[0].upper() or a.name == nodes[i].name.upper() or a.name == nodes[i].name.lower() or a.name == nodes[i].name[0].lower():
        a.name = nodes[i].name
    if b.name == nodes[i].name or b.name == nodes[i].name[0].upper() or b.name == nodes[i].name.upper() or b.name == nodes[i].name.lower() or b.name == nodes[i].name[0].lower():
        b.name = nodes[i].name
state = [0 for i in range(m)]
length = [MAX for i in range(m)]
pre_able = [a for i in range(m)]

node = City
for node in nodes:
    length[dic[node.name]] = matrix[dic[a.name]][dic[node.name]]

node1 = node2 = City
while 0 in state:
    node = a
    dis = MAX
    for node1 in nodes:
        if state[dic[node1.name]] == 0 and length[dic[node1.name]] < dis : 
            dis = length[dic[node_1.name]]
            node = node1
    state[dic[node]] = 1
    for node2 in nodes:
        if state[dic[node2.name]] == 0 and length[dic[node.name]] + matrix[dic[node2.name]][dic[node.name]] < length[dic[node2.name]]:
            length[dic[node2]] = length[dic[node]] + matrix[dic[node2]][dic[node]]
            pre_able[dic[node2.name]] = node
shortest_path = []
node_back = b
while node_back != a:
    shortest_path.append(node_back.name)
    node_back = pre_able[dic[node_back.name]]
shortest_path.append(a.name)
shortest_path2 = shortest_path

index = len(shortest_path)
while index:
    print('shortest path : ',shortest_path.pop(),end = '->')
    index = index - 1
print('')
print('length: ',length[dic[b]])

filename = 'diary.txt'
with open(filename,'a') as file_object:
    file_object.write(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()),' : ','\n','\t','shortest path : ')
    index = len(shortest_path)
    while index:
        file_object.write(shortest_path2.pop(),end = '->')
        index = index - 1