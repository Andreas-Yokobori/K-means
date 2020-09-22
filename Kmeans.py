import numpy as np
import numpy.matlib
import math

a = np.array([1, 2, 3, 4])
b = np.array([2, 3])

A = np.array([[4, 1, 4], [1, 3, 1]])
#print(A)
#print(np.argmin(A, axis=0))

#print(A[[0, 1]])



def kmeans(K, current_means, data):
    #current means: matrix with K rows and n columns (n = dimensions of data)
    #data: m by n matrix (m = number of training points)
    c_i = np.zeros(data.shape[0], 1)
    index = 0
    for d in data: 
        dist = np.sum(np.multiply(d - current_means, d - current_means), axis=1)
        c_i[index] = np.argmin(dist, axis=0)[0]



a = [[11.75962172, 6.69549495], [ 9.18795923,  4.35669971]
 ,[ 9.58067507,  3.89333927]
 ,[ 9.12009337,  5.17099595]
 ,[10.19281906,  5.3240919 ]
 ,[ 9.93193449,  4.54005538]
 ,[10.88794611,  5.76586849]
 ,[ 9.92749213,  4.86919672]
 ,[ 9.34509428,  6.12622897]
 ,[ 9.91843919,  5.5404621 ]
 ,[-2.08936392,  3.7027681 ]
 ,[-2.12107756,  5.3525094 ]
 ,[-4.80742359,  6.31703847]
 ,[-2.68700777,  5.59940515]
 ,[-3.59146553,  5.2457083 ]
 ,[-3.00247675,  4.8694153 ]
 ,[-2.25936507, -6.40817406]
 ,[-2.61423141, -7.63201454]
 ,[-2.85687246, -6.68813515]
 ,[ 0.16331364, -7.07114951]
 ,[-1.71859253, -6.56115321]]

sumx = 0
sumy = 0
for el in a:
    sumx += el[0]
    sumy += el[1]

print(sumx/len(a), sumy/len(a))