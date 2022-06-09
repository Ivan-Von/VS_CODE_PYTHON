import numpy as np
from sympy import *
import sympy
import math
import matplotlib.pyplot as plt
from sympy.simplify.fu import L
import time

Small = 0
Big = 1
def function(x):
    # 得到数学函数
    return (x*sympy.exp(x))/((1+x) ** 2)

def C_C(val): 
    res = 1
    while val>=1:
        res = res*val
        val-=1
    return res

def coefficient(n):
    expression = diff((x**2 -1)**(n+1),x,n+1)
    expression = expression*(1/math.pow(2,n+1))*(1/C_C(n+1))
    return expression

def judgements(x_oringal):
    # 对x不属于[-1,1]进行变换
    if Small ==-1 and Big == 1:
        return x_oringal
    else:
        X_new = (Big - Small)/2 *(x_oringal)+(Small+Big)/2
        return X_new

def calu_n_intergration(x,n,biaoDaShi):
    All_Ak = []
    for val in biaoDaShi:
        # subs()通过替换x ,令x=系数
        A = 2/(1-val**2)/(diff(coefficient(n),x,1).subs(x,val))**2
        All_Ak.append(A)
    length = len(All_Ak)
    temp =0
    for index in range(length):
        # 用evalf函数传入变量的值，对表达式进行求值
        X_location =judgements(biaoDaShi[index])
        temp += (Big-Small)/2*(All_Ak[index]*function(X_location)).evalf()
    return temp


if __name__ == '__main__':
    start = time.time()
    # 指定定义域
    x = symbols('x')
    print("下面是高斯勒让德求积算法")
    Big = 1
    Small = 0
    #integration = Guass.calu_intergration()
    for i in range(20):
        biaoDaShi = solve(coefficient(i))
        integration = calu_n_intergration(x,i,biaoDaShi)
        print("n=",i+1,"高斯勒让德多项式积分：",integration)
    end = time.time()
    print(end - start)