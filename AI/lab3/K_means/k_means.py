import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

# to get distance between point1 and point2
def get_distance(p1, p2):
    diff = [x-y for x, y in zip(p1, p2)]
    distance = np.sqrt(sum(map(lambda x: x**2, diff)))
    return distance

def check(center, new_center):
    for center, new_center in zip(center, new_center):
        if center != new_center:
            return False
    return True

# to get the center of a cluster
def get_center(cluster):
    N = len(cluster)
    x=0;y=0
    for i in range(N):
        x+=cluster[i][0]
        y+=cluster[i][1]
    center_point = [x/N,y/N]
    return center_point

def K_means(points, center_points):
    k = len(center_points) # k = 3
    times = 0

    while True:
        temp_center_points = []
        clusters = []
        for i in range(k):
            clusters.append([])

        # to lable every point
        for i, data in enumerate(points):
            distances = []
            for center_point in center_points:
                distances.append(get_distance(data, center_point))
            index = distances.index(min(distances)) 
            # to find the index of the min distance
            clusters[index].append(data) 
            # add it into the appropriate cluster

        times += 1

        k = len(clusters)
        for i, cluster in enumerate(clusters):
            data = np.array(cluster)
            data_x = [x[0] for x in data]
            data_y = [x[1] for x in data]
            colors = ['r.', 'g.', 'b.','y.']
            plt.subplot(3, 4, times)
            plt.plot(data_x, data_y, colors[i])
            # 这样画不会糊。。。
            plt.axis([0, 10, 0, 6])

        for cluster in clusters:
            temp_center_points.append(get_center(cluster))
 
        for j in range(0, k):
            if len(clusters[j]) == 0:
                temp_center_points[j] = center_points[j]

        for center, new_center in zip(center_points, temp_center_points):
            if not check(center, new_center):
                center_points = temp_center_points[:]
                break
        else:
            break
 
    plt.show()

# to get sample
def get_test_data():
    data = pd.read_csv('AI\\lab3\\K_means\\kmeans_data.csv')
    x1 = data['X1']
    x2 = data['X2']
    points = []
    center_points = []
    for i in range(len(x1)):
        points.append([x1[i],x2[i]])
    # get 3 centers randomly
    for j in range(3):
        k = int(random.uniform(0,300))
        center_points.append([x1[k],x2[k]])
    return points,center_points
 
if __name__ == '__main__':
    points, center_points = get_test_data()
    K_means(points, center_points)