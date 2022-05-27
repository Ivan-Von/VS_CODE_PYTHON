'''
评估函数使用
    1. 权值表：边、角、中心的相对重要程度
    2. 行动力：棋手合法的可能棋步数量
    3. 稳定子：绝对不会被翻转的棋子。例如四角
    事实证明稳定子对程序影响不大，下面进行了删减
'''
import json
import numpy
# eight directions
direction = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))

# 1.
# evaluation map, for showing the importance
# I don't know how to get the chart, it comes from Internet. I guess it's a kind of experience
Vmap = numpy.array(
    [[500,-25,10,5,5,10,-25,500],
    [-25,-45,1,1,1,1,-45,-25],
    [10,1,3,2,2,3,1,10],
    [5,1,2,1,1,2,1,5],
    [5,1,2,1,1,2,1,5],
    [10,1,3,2,2,3,1,10],
    [-25,-45,1,1,1,1,-45,-25],
    [500,-25,10,5,5,10,-25,500]]
)

# to cauclate the position's weight 
def position_weight(board,color):
    return sum(sum(board * Vmap))*color

# 2.
# The possible directions
def execution(board,color):
    # accessible choices
    moves = []
    #what's your usage????????????????
    ValidBoardList = []
    for i in range(8):
        for j in range(8):
            if board[i][j] == 0:
                newboard = board.copy()
                if new_board(newboard,i,j,color):
                    moves.append((i,j))
                    ValidBoardList.append(newboard)
    return moves, ValidBoardList

#3. 
# The pieces that never will be reversed
def getstable(board, color): #稳定子
    stable = [0,0,0]
    # 角, 边, 八个方向都无空格
    cind1 = [0,0,7,7]
    cind2 = [0,7,7,0]
    inc1 = [0,1,0,-1]
    inc2 = [1,0,-1,0]
    stop = [0,0,0,0]
    for i in range(4):
        if board[cind1[i]][cind2[i]] == color:
            stop[i] = 1
            stable[0] += 1
            for j in range(1,7):
                if board[cind1[i]+inc1[i]*j][cind2[i]+inc2[i]*j] != color:
                    break
                else:
                    stop[i] = j + 1
                    stable[1] += 1
    for i in range(4):
        if board[cind1[i]][cind2[i]] == color:
            for j in range(1,7-stop[i-1]):
                if board[cind1[i]-inc1[i-1]*j][cind2[i]-inc2[i-1]*j] != color:
                    break
                else:
                    stable[1] += 1
    colfull = numpy.zeros((8, 8), dtype=numpy.int)
    colfull[:,numpy.sum(abs(board), axis = 0) == 8] = True
    rowfull = numpy.zeros((8, 8), dtype=numpy.int)
    rowfull[numpy.sum(abs(board), axis = 1) == 8,:] = True
    diag1full = numpy.zeros((8, 8), dtype=numpy.int)
    for i in range(15):
        diagsum = 0
        if i <= 7:
            sind1 = i
            sind2 = 0
            jrange = i+1
        else:
            sind1 = 7
            sind2 = i-7
            jrange = 15-i
        for j in range(jrange):
            diagsum += abs(board[sind1-j][sind2+j])
        if diagsum == jrange:
            for k in range(jrange):
                diag1full[sind1-j][sind2+j] = True
    diag2full = numpy.zeros((8, 8), dtype=numpy.int)
    for i in range(15):
        diagsum = 0
        if i <= 7:
            sind1 = i
            sind2 = 7
            jrange = i+1
        else:
            sind1 = 7
            sind2 = 14-i
            jrange = 15-i
        for j in range(jrange):
            diagsum += abs(board[sind1-j][sind2-j])
        if diagsum == jrange:
            for k in range(jrange):
                diag2full[sind1-j][sind2-j] = True
    stable[2] = sum(sum(numpy.logical_and(numpy.logical_and(numpy.logical_and(colfull, rowfull), diag1full), diag2full)))
    return stable

# get evaluation
def evaluation(moves,board,color):
    moves_avaiable, ValidBoardList = execution(board,-color)
    value = position_weight(board,color) + 15* (len(moves)-len(moves_avaiable))
    return value
    

# if there are all 1 or all -1
def special(board,color):
    for i in range(8):
        for j in range(8):
            if board[i][j] == -color:
                return False
    return True

# to make sure the coord is reasonable
def reasonable(x,y):
    return x>=0 and x<8 and y>=0 and y<8

# to place new chess pieces to the chosen place and update the board
def new_board(board,x,y,color):
    if x < 0 or y < 0:
        return False
    board[x][y] = color
    valid = False
    for d in range(8):
        # search the eight directions one by one 
        i = x + direction[d][0]
        j = y + direction[d][1]
        # reverse the pieces with the opposite color
        while reasonable(i,j) and board[i][j] == -color:
            i += direction[d][0]
            j += direction[d][1]
        if reasonable(i,j) and board[i][j] == color:
            while True:
                i -= direction[d][0]
                j -= direction[d][1]
                if i == x and j == y:
                    break
                valid = True
                board[i][j] = color
    return valid


def Alpha_Beta(board,depth,alpha,beta,actcolor,mycolor,maxdepth):
    moves,ValidBoardList = execution(board, actcolor)
    if len(moves) == 0:
        return evaluation(moves,board,mycolor),(-1,-1)
    if depth == 0:
        return evaluation(moves,board,mycolor),[]
    
    if depth == maxdepth:
        for i in range(len(moves)):
            if Vmap[moves[i][0]][moves[i][1]] == Vmap[0][0] and actcolor == mycolor:
                return 1000,moves[i]
        if depth >= 4:
            Vmoves = []
            for i in range(len(ValidBoardList)):
                value, bestmove = Alpha_Beta(ValidBoardList[i], 1, -10000, 10000, -actcolor, mycolor, maxdepth)
            Vmoves.append(value)
        ind = numpy.argsort(Vmoves)
        maxN = 6
        moves = [moves[i] for i in ind[0:maxN]]
        ValidBoardList = [ValidBoardList[i] for i in ind[0:maxN]]
    
    bestmove = []
    bestscore = -10000
    for i in range(len(ValidBoardList)):
        score, childmove = Alpha_Beta(ValidBoardList[i], depth-1, -beta, -max(alpha, bestscore), -actcolor, mycolor, maxdepth)
        score = -score
        if score > bestscore:
            bestscore = score
            bestmove = moves[i]
            if bestscore > beta:
                return bestscore, bestmove
    return bestscore, bestmove

def onestepplace(board, mycolor):
    stage = sum(sum(abs(board)))
    if stage <= 9:
        depth = 5
    elif stage >= 50:
        depth = 6
    # elif stage == 63:
    #     depth = 64
    else:
        depth = 4
    value, bestmove = Alpha_Beta(board, depth, -10000, 10000, mycolor, mycolor, depth)
    return bestmove


def end(board):
    for i in range(8):
        for j in range(8):
            if board[i][j] == 0:
                return True
    return False


board = numpy.zeros((8,8),dtype=numpy.int)
board[3][4] = board[4][3] = 1 #白
board[3][3] = board[4][4] = -1 #黑
AIColor = 1

print("Begin. Good Luck\n",board)
while(end(board)):
    if(special(board,AIColor)):
        print("No place to lay. You lost")
        break
    elif(special(board,-AIColor)):
        print("AI has no place to lay. You win")
        break
    move = onestepplace(board,AIColor)
    x,y = move
    print("The AI chose :",move)
    new_board(board,x,y,1)
    print("After AI, the score is:",sum(sum(board)),"\nand the board is:")
    print(board)
    moves = execution(board,-AIColor)
    print("Accesssible choice:")
    print(moves[0])
    if moves[0] == []:
        input("No place to lay")
        continue
    else:
        i = input("Where to lay")
        # the order can not be changed
        if not i.isdigit() or int(i) >= len(moves[0]) or int(i) < 0:
            print("WARNING! IILEGAL INPUT. YOU LOST AN CHANCE!")
        else:
            yourmove = moves[0][int(i)]
            new_board(board,yourmove[0],yourmove[1],-AIColor)
            print("After Your choice, the score is:",sum(sum(board)),"\nand the board is:")
            print(board)

score = sum(sum(board))
if score < 0:
    print("You keep more than AI. You win")
elif score == 0:
    print("DEUCE")
else:
    print("AI keeps more than you. You lost")