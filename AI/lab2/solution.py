import copy
from opposite import opposite

def solution(V,M,S,cot):
    #global S
    #global cot
    #print(len(S))
    end = False
    while True:
        if end: break 
        father = S.pop()
        jflag=False #判断函数的可合成性
        for i,val in father.items(): #i是索引，val是里面的值
            if end: break
            for mother in S:
                #print("mother",mother)
                if end: break
                j=[]
                pos2=''
                pos3=''
                for key,value in mother.items(): #一个意思，key是索引，value是里面的值
                    if key==opposite(i):#大前提
                        dif=0#判断不同的谓词有多少个
                        for pos1 in value:#mother里面的变量
                            if pos1 in val:
                                continue
                            else:
                                dif+=1
                                pos2=pos1#记录不同的谓词
                        if dif<=1:#说明可以进行合成
                            for h in range(len(val)):#一种思路是找变量x,y,z，最开始的想法，但是会全盘替换，难以实现，此思路为直接判断不同的谓词有几个，确实有问题
                                if val[h] in value:#存在一样的就跳过
                                    continue
                                else:
                                    pos3=val[h]#记录father和mother里面不同的那个变量
                                    #print("pos3",pos3)
                            flag=True#说明可以合成
                            #print("V",V)
                            for key1 in V.values():#如果这个函数已经被替换过了，就不可再替换，为了修正82行的错误
                                if pos2 ==key1:
                                    flag=False
                                    break
                            if flag==True:
                                j.append(key) #记录每次取到的可替换函数
                                break
                if j == []:
                    continue
                else:
                    jflag=True#j不是空的，修改标志位为可替换
                    #print('R[',father['posnum'],',',mother['posnum'],'] = ',end=' ')
                    print('R[',end='')
                    m=0#为了确定输出里面的字母
                    for k1 in father.keys():
                        if k1==i:
                            break
                        m+=1
                    n=0#同理
                    for k2 in mother.keys():
                        if k2==key:
                            break
                        n+=1
                    print(father['posnum'],end='')
                    if len(father)>2:#忘了为什么判断这个了
                        print(M[m],end='')
                    print(',',end='')
                    print(mother['posnum'],end='')
                    if len(mother)>2:
                        print(M[n],end='')
                    print(']',end='')
                    if pos2!='' and pos3!='':
                        print('(',end='')
                        print(pos3,'=',pos2,end='')
                        print(') ',end='')
                    print('= ',end='')
                    newele1={}
                    newele2={}
                    newele1=copy.deepcopy(father)
                    newele2=copy.deepcopy(mother)
                    if pos2!='' and pos3!='':
                        V[pos2]=pos3
                        for vk,v in newele1.items():
                            if vk=='posnum':
                                break
                            for k in range(len(v)):
                                if v[k]==pos3:
                                    v[k]=pos2
                    del newele1[i]
                    del newele2[j[0]]
                    if len(newele1)>1:
                        newele1['posnum']=cot
                        cot+=1
                        S.append(newele1) 
                    if len(newele2)>1:
                        newele2['posnum']=cot
                        cot+=1
                        S.append(newele2)
                    S.remove(mother)
                    if len(newele1) == 1 and len(newele2) == 1:
                        print('[]')
                        end = True
                    elif len(newele1) == 1:
                        cot2=0 
                        for key,value in newele2.items():
                            if key=='posnum':
                                break
                            print(key,'(',end='')
                            for m in range(len(value)):
                                print(value[m],end='')
                                if m!=len(value)-1:
                                    print(',',end='')
                            print(')',end='')
                            if cot2!=len(newele2)-2:
                                print(',',end='')
                            cot2+=1
                        print('\n',end='')
                    elif len(newele2) == 1:
                        cot2=0 
                        for key,value in newele1.items():
                            if key=='posnum':
                                break
                            print(key,'(',end='')
                            for m in range(len(value)):
                                print(value[m],end='')
                                if m!=len(value)-1:
                                    print(',',end='')
                            print(')',end='')
                            if cot2!=len(newele1)-2:
                                print(',',end='')
                            cot2+=1
                        print('\n',end='')
                    else:
                        cot2=0 
                        cot3=0
                        for key,value in newele1.items():
                            if key=='posnum':
                                break
                            print(key,'(',end='')
                            for m in range(len(value)):
                                print(value[m],end='')
                                if m!=len(value)-1:
                                    print(',',end='')
                            print(')',end='')
                            if cot2!=len(newele1)-2:
                                print(',',end='')
                            cot2+=1
                        print(' and',end=' ')
                        for key,value in newele2.items():
                            if key=='posnum':
                                break
                            print(key,'(',end='')
                            for m in range(len(value)):
                                print(value[m],end='')
                                if m!=len(value)-1:
                                    print(',',end='')
                            print(')',end='')
                            if cot3!=len(newele2)-2:
                                print(',',end='')
                            cot3+=1
                        print('\n',end='')
        if jflag==False:
            S.insert(0,father)