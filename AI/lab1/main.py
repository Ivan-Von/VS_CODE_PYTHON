from func import *
#无向图数据：开始计算最短路径用的rout来存储结构，后来网络分析模块必须要rout_list格式制作权值表
# 由于不想统一成rout_list,因为要改算法，就没管，路径数据保留了两份，等以后有时间了再改
rout = {'AB':12,'AG':14,'AF':16,'BF':7,'BC':10,'GF':9,\
        'GE':8,'CF':6,'EF':2,'CD':3,'CE':5,'ED':4}
rout_list = [('A','B',12),('A','G',14),('A','F',16),('B','F',7),\
             ('B','C',10),('G','F',9),('G','E',8),('C','F',6),\
             ('E','F',2),('C','D',3),('C','E',5),('E','D',4)]
 
inf = float('inf')#无穷大
cloest_rout = [['D']]
S = {'D':0}  #确定最短路径集合
U = {'A':inf,'B':inf,'C':inf,'E':inf,'F':inf,'G':inf} #未确定的最短路径集合
 
while(U != {}): #直到未确定最短路径为空，才最终确定完最短路径
    findCloestrout(inf,rout,S,U,cloest_rout)
 
for list1 in cloest_rout:
    print(list1[-1]+':',end='')
    print('->'.join(list1))
print('最短路径集合：',S)
draw(rout,rout_list)
 
 