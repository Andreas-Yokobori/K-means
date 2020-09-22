import random
import matplotlib.pyplot as plt
import numpy as np
#%matplotlib inline

from Cluster import Cluster

clusters = [(10, 5, 10), (-3, 5, 6), (-2, -7, 5)]
clusterList = []
shape1 = 0
for c in clusters:
    clusterList.append(Cluster(*c))
    shape1 += c[2]

points = np.zeros(shape=(2, shape1))

start = 0
for cl in clusterList:
    points[0, start:start + cl.getSize()] = np.random.normal(loc=cl.getX(), size=cl.getSize())
    points[1, start:start + cl.getSize()] = np.random.normal(loc=cl.getY(), size=cl.getSize())
    start += cl.getSize()
#print(points)

plt.scatter(points[0], points[1])


data = np.transpose(points)

def kmeans(K, data, current_means):
    #current means: matrix with K rows and n columns (n = dimensions of data)
    #data: m by n matrix (m = number of training points)
    c_i = np.zeros((data.shape[0], 1))
    #print("c_i: \n", c_i)
    index = 0
    for d in data: 
        dist = np.sum(np.multiply(d - current_means, d - current_means), axis=1)
        #print("dist: \n", dist)
        c_i[index] = np.argmin(dist)
        index += 1
    #print(np.squeeze(c_i == 2))
    #print(data[np.squeeze(c_i == 2)])
    for i in range(K):
        print(np.mean(data[np.squeeze(c_i == i)]))
        current_means[i] = np.mean(data[np.squeeze(c_i == i)])
    print(current_means)


current_means = np.array([[-1, -1], [0, 0], [5, 5]])
print("data: \n", data)
#print(current_means)

K = 3
kmeans(K, data, current_means)


#plt.show()

'''
def generate_cluster(loc1, loc2, size):
    return ((loc1, loc2), size)

cluster1 = generate_cluster(10, 5, 10)
cluster2 = generate_cluster(-3, 5, 6)
cluster3 = generate_cluster(-2, -7, 5)

x = np.random.normal(loc=cluster1[0][0], size=cluster1[1])
y = np.random.normal(loc=cluster1[0][1], size=cluster1[1])

x = np.concatenate((x, np.random.normal(loc=cluster2[0][0], size=cluster2[1])))
y = np.concatenate((y, np.random.normal(loc=cluster2[0][1], size=cluster2[1])))

x = np.concatenate((x, np.random.normal(loc=cluster3[0][0], size=cluster3[1])))
y = np.concatenate((y, np.random.normal(loc=cluster3[0][1], size=cluster3[1])))

plt.scatter(x, y)

#plt.hist(x, density=True, bins=30)  # `density=False` would make counts
#plt.ylabel('Probability')
#plt.xlabel('Data')



plt.show()
'''