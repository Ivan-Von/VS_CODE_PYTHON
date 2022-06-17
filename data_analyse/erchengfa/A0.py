import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import time
start = time.time()
x_arr = []
for i in range(19):
    x_arr.append(i+1)
y_arr = [0.90,2.38,3.07,1.84,2.02,1.94,2.22,2.77,4.02,4.76,5.46,6.53,10.9,16.5,22.5,35.7,50.6,61.6,81.8]
def exp_fun(x,a,b):
    return (a * np.exp(b*x))
def exp_fun2(x,a,b,c):
    return (a * np.exp(b*x) + c)
plt.plot(x_arr,y_arr,'b')
#plt.scatter(x_arr,y_arr)
popt,pcov = curve_fit(exp_fun,x_arr,y_arr)
popt2,pcov = curve_fit(exp_fun2,x_arr,y_arr)
index = 0
for i in range(len(x_arr)):
    index += pow((exp_fun(i,popt[0],popt[1])-y_arr[i]),2)
print(index)
index1 = 0
for i in range(len(x_arr)):
    index1 += pow((exp_fun2(i,popt2[0],popt2[1],popt2[2]))-y_arr[i],2)
print(index1)
end = time.time()
print('time',end - start)
y2 = [exp_fun(i,popt[0],popt[1]) for i in np.linspace(1,19,100)]
y3 = [exp_fun2(i,popt2[0],popt2[1],popt2[2]) for i in np.linspace(1,19,100)]
plt.plot(np.linspace(1,19,100), y2, 'r--')
plt.plot(np.linspace(1,19,100), y3, 'g--')
plt.ylabel('incidence rate y‰')
plt.xlabel('age x')
plt.show()

