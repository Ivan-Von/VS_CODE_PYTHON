from cProfile import label
from distutils.log import error
from sympy.abc import x
from sympy import integrate, exp, diff
import sympy
import numpy as np
from math import factorial, pow
import numpy as np
import matplotlib.pyplot as plt
import normalGL
import Newton_Contes
import sympy
from scipy.optimize import curve_fit 
TrueValue = 0.3591409142295226
if __name__ == '__main__':
    x_arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    y_arr0 = [TrueValue for i in range(len(x_arr))]
    y_arr1 = [0.339785228557381,0.357516745919146,0.358371369473132,0.359090676284142,0.359111668989954,0.359138843139403,0.359139609482638,0.359140817032077,0.359140850410140,0.359140909338611,0.359140910935464,0.359140913972595,0.359140914053477,0.359140914215628,0.359140914219883,0.359140914228755,0.359140914228985,0.359140914229479,0.359140914229493,0.359140914229525]
    y_arr2 = [0.366382504600028,0.360176745097282,0.359187170340175,0.359142699259551,0.359140979168727,0.359140916505945,0.359140914307274,0.359140914232128,0.359140914229609,0.359140914229525,0.359140914229523,0.359140914229523,0.359140914229523,0.359140914229522,0.359140914229523,0.359140914229523,0.359140914229524,0.359140914229524,0.359140914229522,0.359140914229522]
    # plt.scatter(x_arr,y_arr1,label='Newton_Contes')
    # plt.scatter(x_arr,y_arr0,label='TrueValue')
    # plt.scatter(x_arr,y_arr2,label='Gauss_Lengendre')
    # plt.legend()
    error1 = []
    error2 = []
    for i in range(20):
        error1.append(abs(y_arr1[i]-TrueValue))
        error2.append(abs(y_arr2[i]-TrueValue))
    plt.plot(x_arr,error1,label = 'NC error')
    plt.plot(x_arr,error2,label = 'GL error')
    # plt.plot(x_arr,y_arr1,label='Newton_Contes')
    # plt.plot(x_arr,y_arr0,label='TrueValue')
    # plt.plot(x_arr,y_arr2,label='Gauss_Lengendre')
    plt.legend()
    plt.show()
