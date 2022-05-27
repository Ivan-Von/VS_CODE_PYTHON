direction=[(0,1),(1,0),(0,-1),(-1,0)]
path = []
matrix = []

def read(filePath):
    with open(filePath, encoding='utf-8') as file_obj:
        for line in open(filePath,encoding='utf-8'):
            line = line.strip()
            line = list(line)
            matrix.append(line)

class Node:
    def __init__(self,state,pre) -> None:
        self.state = state
        self.pre = pre
        self.cost = 1
def frontier(state):
    