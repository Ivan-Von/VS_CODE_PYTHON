path1 = []
path2 = []
matrix = []
visit = []
direction = [(0,1),(1,0),(0,-1),(-1,0)]#表示上下左右四个方向
def __dbfs__(start,end):
    t = (0,0)
    path1.append(start)
    path2.append(end)
    while(len(path1) & len(path2)):
        if(len(path1) > len(path2)):
            t = path2.pop()
            flag = 0
        else:
            t = path1.pop()
            flag = 1
        for i in range(4):
            pos = t[0] + direction[i][0] , t[1] + direction[i][1]
            if pos[0] >=1 & pos[0] <= end[0] & pos[1] >= 1 & pos[1] <= end[1] & matrix[pos[0]][pos[1]] == 0 :
                if (visit[pos[0]][pos[1]] == 0):
                    if flag:
                        path1[pos[0]][pos[1]] = 1
                        visit[pos[0]][pos[2]] = visit[t[0]][t[1]] + 1
                        path1.append((pos[0],pos[1]))
                    else:
                        path1[pos[0]][pos[1]] = 2
                        visit[pos[0]][pos[2]] = visit[t[0]][t[1]] + 1
                        path2.append((pos[0],pos[1]))
                else:
                    if visit[pos[0]][pos[1]] + visit[t[0]][t[1]] == 3:
                        return 

