import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import sympy
import math
x_arr = []
y_arr = [0.90,2.38,3.07,1.84,2.02,1.94,2.22,2.77,4.02,4.76,5.46,6.53,10.9,16.5,22.5,35.7,50.6,61.6,81.8]
y_arr0 = [0.90,2.38,3.07,1.84,2.02,1.94,2.22,2.77,4.02,4.76,5.46,6.53,10.9,16.5,22.5,35.7,50.6,61.6,81.8]

for i in range(len(y_arr)):
    x_arr.append(i+1)
    y_arr[i] = math.log(y_arr[i])
def exp_fun(x,a,b):
    return (a * np.exp(b*x))

temp00 = len(y_arr)
temp10 = sum(x_arr)
temp11 = 0
for i in range(len(x_arr)):
    temp11 += x_arr[i] ** 2

temp_0y = sum(y_arr)
temp_1y = 0
for i in range(len(x_arr)):
    temp_1y += x_arr[i] * y_arr[i]

# 解方程
B = (temp_1y-(temp10*temp_0y)/temp00)*1.0 / (temp11-(temp10*temp10)/temp00)
A = (temp_0y-temp10*B)/temp00
A = np.exp(A)
print(A,B)
y2_arr = []
for i in range(len(x_arr)):
    y2_arr.append(exp_fun(i+1,A,B))

# plt.plot(x_arr,y_arr0,'b--')
# #plt.scatter(x_arr,y_arr0)
# plt.plot(x_arr,y2_arr,'r--')
# plt.show()
index = 0
for i in range(len(x_arr)):
    index += pow((y2_arr[i]-y_arr0[i]),2)
print(index)