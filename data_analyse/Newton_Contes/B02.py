import numpy as np
import math
from sympy import *

# # to get the coefficient
# def contes_coefficient():

# # to get every node
# def contes_nodes(a,b,n):
#     x_array = []
#     h = (b-1)/n
#     for i in range(n):
#         x_array.append(a+i*h)
#     return x_array

# def New_Contes():




def C(n=int(), k=int()):
    if (n - k) % 2 == 0:
        ans = 1
    else:
        ans = -1
    for j in range(n+1):
        if j != k:
            ans *= (x - j)
    ans = integrate(ans, (x, 0, n)) / n
    for i in range(k):
        ans /= (i+1)
    for i in range(n-k):
        ans /= (i+1)
    print(ans, end=' ')


if __name__ == '__main__':
    x = symbols('x')
    for i in range(8):
        for j in range(i+2):
            C(i+1, j)
        print()