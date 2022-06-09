import math
from symtable import Symbol
import numpy as np
from sympy import*
"""
牛顿科特斯插值积分公式的实现
f_x:待积分函数
New_Cotes:积分函数
a,b:积分区间
n:求积节点个数
1<=n<=7最好,8开始会有负数导致结果不准确
原公式中n为等分的区间个数,这里是等分点的个数，所以使用
"""
'''
def f_x(x):
    return (x*np.exp(x))/(math.pow(1+x,2))
'''
'''
def New_Cotes(n,a,b,x,f_x):
    n+=1
    step = (b-a)/(n)
    k_array = np.array([f_x.subs(x, a + k*step) for k in range(n+1)])
    return (b-a)*np.sum(cotes_coefficient(n,x)*k_array)
def cotes_coefficient(n,t):
    n+=1
    k_array = np.zeros(n+1, dtype=np.float64)
    for k in range(n+1):
        index = list(range(n+1))
        index.pop(k)
        intergrand = np.prod(t - np.array(index))
        intergral = intergrate(intergrand,(t,0,n))
        k_array[k] = (-1)**(n - k)/(n*math.factorial(k)*math.factorial(n-k))
    return k_array
'''
def newtown_cotes_integrate(equal_segment, interval_start, interval_end, symbol_t, f_x):
    """
    实现牛顿-柯特斯(Newton-Cotes)插值型积分
    :param symbol_t: 引进变换x=a+t*h后的积分变量
    :param equal_segment: 区间等分数n
    :param interval_start: 区间左端点即起点
    :param interval_end: 区间右端点即终点
    :param f_x: 被积函数 intergrand
    :return:牛顿-柯特斯(Newton-Cotes)插值积分
    """
    step_h = (interval_end - interval_start) / equal_segment
    f_k_array = np.array([f_x.subs(x, interval_start + k * step_h) for k in range(equal_segment + 1)])
    return (interval_end - interval_start) * np.sum(cotes_coefficient(equal_segment, symbol_t) * f_k_array)


def cotes_coefficient(equal_segment, symbol_t):
    """
    实现牛顿-柯特斯(Newton-Cotes)插值型求积公式的柯特斯系数
    :param equal_segment: 区间等分数n,其中1<=n<=7,n>7的牛顿-柯特斯公式计算不稳定，不使用.
    :param symbol_t: 引进变换x=a+t*h后的积分变量t
    :return: 柯特斯系数数组
    """
    if equal_segment not in range(1, 8):
        raise ValueError("Cotes coefficient must be an integer between 1 and 7")
    c_k_array = np.zeros(equal_segment + 1, dtype=np.float64)
    for k in range(equal_segment + 1):
        index = list(range(equal_segment + 1))
        index.pop(k)
        intergrand = np.prod(symbol_t - np.array(index))
        integral = integrate(intergrand, (symbol_t, 0, equal_segment))
        c_k_array[k] = (-1) ** (equal_segment - k) / (
                equal_segment * factorial(k) * factorial(equal_segment - k)) * integral
    return c_k_array
if __name__ == '__main__':
    # 辛普森公式及其余项表达式测试成功，来源详见来源详见李庆扬数值分析第5版P135,e.g.4
    # 0.632333680003663
    inter_grand = exp(-x)
    print("辛普森公式积分为:{}".format(newtown_cotes_integrate(2, 0, 1, x, inter_grand)))
    # print("辛普森公式为:{}".format(quadrature_reminder(a=0, b=1, equal_segment=2, m=3, intergrand=exp(-x), a_k=cotes_coefficient(2, x))[0]))
    # # 复合梯形公式和复合辛普森公式测试成功，来源详见来源详见李庆扬数值分析第5版P135,e.g.2(1)
    # f_x = x / (4 + x ** 2)
    # print("复合梯形公式积分:{}".format(com_trapz(a=0, b=1, equal_segment=8, intergrand=f_x)))  # 0.111402354529548
    # print("复合辛普森公式积分:{}".format(com_simpson(a=0, b=1, equal_segment=8, intergrand=f_x)))  # 0.111571813252631


#要等分n份，则需要n-1个点，所以计算时n全部加一才是份数
x_array = []
def x_define(a,b,n):
    n+=1
    h = (b-1)/n
    for i in range(n):
        x_array.append(a+i*h)
