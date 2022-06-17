import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

data = pd.read_csv('AI\\lab3\\K_means\\kmeans_data.csv')
x1 = data['X1']
x2 = data['X2']
points = []
center_points = []
for i in range(len(x1)):
    points.append([x1[i],x2[i]])

for i in range(len(x1)):
    plt.scatter(points[i][0],points[i][1],c='g')
plt.show()