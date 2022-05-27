S = [] # 以列表形式存储子句集S


"""
读取子句集文件中子句，并存放在S列表中
    - 每个子句也是以列表形式存储
    - 以析取式分割
    - 例如：～p ∨ ～q ∨ r 存储形式为 ['～p', '～q', 'r']
"""
def readClauseSet(filePath):
    global S
    for line in open(filePath, mode = 'r', encoding = 'utf-8'):
        line = line.replace(' ', '').strip()
        line = line.split('∨')
        S.append(line)


"""
- 为正文字，则返回其负文字
- 为负文字，则返回其正文字
"""
def opposite(clause):
    if '～' in clause:
        return clause.replace('～', '')
    else:
        return '～' + clause


"""
归结
"""
def resolution():
    global S
    end = False
    while True:
        if end: break
        father = S.pop()
        for i in father[:]:
            if end: break
            for mother in S[:]:
                if end: break
                j = list(filter(lambda x: x == opposite(i), mother))
                if j == []:
                    continue
                else:
                    print('\n亲本子句：' + ' ∨ '.join(father) + ' 和 ' + ' ∨ '.join(mother))
                    father.remove(i)
                    mother.remove(j[0])
                    if(father == [] and mother == []):
                        print('归结式：NIL')
                        end = True
                    elif father == []:
                        print('归结式：' + ' ∨ '.join(mother))
                    elif mother == []:
                        print('归结式：' + ' ∨ '.join(mother))
                    else:
                        print('归结式：' + ' ∨ '.join(father) + ' ∨ ' + ' ∨ '.join(mother))
                   

def ui():
    print('----')
    print('--------命题逻辑归结推理系统--------')
    print('----')


def main():
    filePath = r'input4.txt'
    readClauseSet(filePath)
    ui()
    resolution()


if __name__ == '__main__':
    main()
