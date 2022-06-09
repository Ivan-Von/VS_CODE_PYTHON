from sympy.abc import x
from sympy import integrate, exp, diff
import sympy
import numpy as np
from math import factorial, pow
import math
import time

def quadrature_reminder(a, b, n, m, intergrand, a_k: np.ndarray):
    """
    实现[a,b]代数精度为m的求积公式余项表达式
    :param a: 区间左端点即起点a
    :param b: 区间右端点即终点b
    :param n: 区间等分数n
    :param m: 代数精度m
    :param intergrand: 被积函数f(x)
    :param a_k: 权系数Ak数组
    :return: 求积公式余项表达式
    """
    step_h = (b - a) / n
    f_x = x ** (m + 1)
    f_x_k_array = np.array([f_x.subs(x, a + k * step_h) for k in range(n + 1)])
    return 1 / factorial(m + 1) * (1 / (m + 2) * (b ** (m + 2) - a ** (m + 2)) - np.sum(a_k * f_x_k_array)) * diff(
        intergrand, x, m + 1), a, b



def newtown_cotes_integrate(n, a, b, symbol_t, f_x):
    """
    实现牛顿-柯特斯(Newton-Cotes)插值型积分
    :param symbol_t: 引进变换x=a+t*h后的积分变量
    :param n: 区间等分数n
    :param a: 区间左端点即起点
    :param b: 区间右端点即终点
    :param f_x: 被积函数 intergrand
    :return:牛顿-柯特斯(Newton-Cotes)插值积分
    """
    step_h = (b - a) / n
    f_k_array = np.array([f_x.subs(x, a + k * step_h) for k in range(n + 1)])
    return (b - a) * np.sum(cotes_coefficient(n, symbol_t) * f_k_array)


def cotes_coefficient(n, symbol_t):
    """
    实现牛顿-柯特斯(Newton-Cotes)插值型求积公式的柯特斯系数
    :param n: 区间等分数n,其中1<=n<=7,n>7的牛顿-柯特斯公式计算不稳定，不使用.
    :param symbol_t: 引进变换x=a+t*h后的积分变量t
    :return: 柯特斯系数数组
    """
    c_k_array = np.zeros(n + 1, dtype=np.float64)
    for k in range(n + 1):
        index = list(range(n + 1))
        index.pop(k)
        intergrand = np.prod(symbol_t - np.array(index))
        integral = integrate(intergrand, (symbol_t, 0, n))
        c_k_array[k] = (-1) ** (n - k) / (
                n * factorial(k) * factorial(n - k)) * integral
    return c_k_array

if __name__ == '__main__':
    start = time.time()
    inter_grand = (x*sympy.exp(x))/((1+x) ** 2)
    x_arr = []
    y_arr = []
    for i in range(20):
        y = newtown_cotes_integrate(i+1, 0, 1, x, inter_grand)
        x_arr.append(i+1)
        y_arr.append(y)
        print("n=",i+1,"牛顿科特斯公式积分为",y)
    end = time.time()
    print(end-start)
    #print("辛普森公式为:{}".format(quadrature_reminder(a=0, b=1, n=2, m=3, intergrand=inter_grand, a_k=cotes_coefficient(2, x))[0]))
