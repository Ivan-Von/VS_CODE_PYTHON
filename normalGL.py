#高斯-勒让德求积公式
from sympy import *
import time
import sympy
from scipy.special import perm,comb  #排列,组合
x,t = symbols("x,t")
#积分区间
a = 0
b = 1
#需要求积的目标函数
def f(x):
    return (x*sympy.exp(x))/((1+x) ** 2)

# n = 4
#n次多项式正交，n越大精度越高(n=0,1,2,...)
#勒让德多项式
def L(n):
    df = diff((x ** 2 - 1) ** (n + 1), x, n + 1)
    # Python内置阶乘函数factorial
    L = 1 /2**(n+1)/factorial(n+1) * df
    return L

#高斯点x求取
def Gauss_point(n):
    x_k_list = solve(L(n))   #求得零点解集
    return x_k_list

#求积系数A
def Quadrature_coefficient(x_k_list):
    A_list = []
    for x_k in x_k_list:
        A = 2/(1-x_k**2)/(diff(L(n),x,1).subs(x,x_k))**2
        A_list.append(A)
    return A_list
if __name__ == '__main__':
    start = time.time()
    for n in range(20):
        if n== 5 or n==6:
            continue
        result = 0
        x_k_list = Gauss_point(n)
        A_list = Quadrature_coefficient(Gauss_point(n))
        sum = len(A_list)
        #区间变换
        if a == -1 and b == 1:
            for i in range(sum):
                result += (A_list[i] * f(x_k_list[i])).evalf()
        #将求求粉公式中的区间(a,b)转换为[-1,1]
        else:
            for i in range(sum):
                X = (b-a)/2 * x_k_list[i] + (a+b)/2  #区间变换
                result += (b-a)/2 * (A_list[i] * f(X)).evalf()
        print("n=",n,"Gauss_Lengendre result",result)
    end = time.time()
    print(end-start)