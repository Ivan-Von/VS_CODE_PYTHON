def readClauseSet(filePath,S,cot):
    #global S #字典，用来记录每一行的谓词和变量
    #global cot 
    for line in open(filePath,encoding = 'utf-8'):
        line = line.replace(' ', '').strip() #先把空格和不可见字符（如换行）去掉
        #print(line)
        if line[0]=='(': #如果是最后一行
           line=list(line) #把字符串变成了list，便于操作
           line[0]='' #去掉头尾两个括号
           line[len(line)-1]=''
           line=''.join(line) #因为是''.join所以相当于加起来
        for i in range(len(line)-2):#因为替换了两个头尾，所以缩短
            if line[i+1]==','and line[i]==')':#这里也是处理最后一行，为了把多个函数分开
                line=list(line) 
                line[i+1]=';' #改变符号是为了后面进行split
                line=''.join(line) 
                #print(line)
        line = line.split(';') #通过;来分割字符串,每个分到元组元素中,为了和前几行做区分使用了;
        #print(line)
        newele={}
        for i in range(len(line)): 
            str1=line[i] #每次读入的元素
            for j in range(len(str1)-1):
                str2=str1#为了不改变str1的值，做一个保留
                if str1[j]=='(':
                   elename=str2[0:j] #找到了函数谓词名称
                   elemem=str2[j+1:len(str1)-1] #用到了str1,elemem是剩下的字符串
                   elemem=elemem.split(',')#分割开
                   newele[elename]=elemem#填充字典，比如'On': ['aa', 'bb']
                   line[i]=newele
                   break
        newele['posnum']=cot #这个参数对应行数
        #例如第一行执行完之后newele里面是{'On': ['aa', 'bb'], 'posnum': 1}
        cot+=1 #记录行数
        S.append(newele) #可以将S认为是二维字典元组，S最后应该是[{'On': ['aa', 'bb'], 'posnum': 1}, {'On': ['bb', 'cc'], 'posnum': 2}, {'Green': ['aa'], 'posnum': 3}, {'!Green': ['cc'], 'posnum': 4}, {'!On': ['x', 'y'], '!Green': ['x'], 'Green': ['y'], 'posnum': 5}]
        #print("\n S here")
        #print(S)