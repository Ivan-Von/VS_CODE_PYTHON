import numpy as np
from sympy import *
import sympy
import math
import matplotlib.pyplot as plt
from sympy.simplify.fu import L
import time

class Guass:
    def __init__(self,Small,Big,x):
        self.Small = Small 
        self.Big = Big
        self.x = x
        
    def function(self,x):
        # 得到数学函数
        return (x*sympy.exp(x))/((1+x) ** 2)
     
    def calu_n_intergration(self,n,biaoDaShi):
        # 算n=1,2,3,4,5,6,7,8,9的对应积分值
        All_Ak = []
        for val in biaoDaShi:
            # subs()通过替换x ,令x =系数
            A = 2/(1-val**2)/(diff(self.coefficient(n),self.x,1).subs(self.x,val))**2
            # print(val,A,end ='\t')
            All_Ak.append(A)
            
        length = len(All_Ak)    
        temp =0
        # 对上界和下界不为1，-1的进行处理
        
        for index in range(length):
            # 用evalf函数传入变量的值，对表达式进行求值
            X_location =self.switch(biaoDaShi[index])
            temp += (self.Big-self.Small)/2*(All_Ak[index]*self.function(X_location)).evalf()
        
        return temp

    def switch(self,x_oringal):
        # 对x不属于[-1,1]进行变换
        if self.Small ==-1 and self.Big == 1:
            return x_oringal
        else:
            X_new = (self.Big - self.Small)/2 *(x_oringal)+(self.Small+self.Big)/2
            return X_new

    def coefficient(self,n):
        expression = diff((self.x**2 -1)**(n+1),x,n+1)
        expression = expression*(1/math.pow(2,n+1))*(1/self.C_C(n+1))
        return expression
    
    # 算n!
    def C_C(self,val): 
        res = 1
        while val>=1:
            res = res*val
            val-=1
        return res
    
    def calu_trueValue(self):
        res = integrate((self.x*sympy.exp(self.x))/((1+self.x) ** 2),(self.x,self.Small,self.Big))
        return res
        
if __name__ == '__main__':
    # 指定定义域
    start = time.time()
    x = symbols('x')
    print("下面是高斯勒让德求积算法")
    Big = 1
    Small = 0
    Guass = Guass(Small,Big,x)
    #integration = Guass.calu_intergration()
    for i in range(20):
        biaoDaShi = solve(Guass.coefficient(i))
        integration = Guass.calu_n_intergration(i,biaoDaShi)
        print("n=",i+1,"高斯勒让德多项式积分：",integration)
    end = time.time()
    print(end-start)
    # true_value = Guass.calu_trueValue()
    # print(f"最后的计算结果:{integration}")
    # print(f"真实值：{true_value}")
    # print("误差：{}".format(math.fabs(true_value - integration)))