import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
a = np.array([10, 12, 14, 16, 18, 20, 22, 24, 25, 28])
b = np.array([1, 5, 10, 15, 20, 25, 30, 35, 40, 45])
c2 = []
d2= []
n = 10
c = np.mean(a)
d = np.mean(b)
for i in range(len(a)):
    c2.append(a[i])
for j in range(len(b)):
    d2.append(b[j])
print(-(c+d/2)*.00001)
plt.plot(a,b,'black')
SS_xy = np.sum(b*a) - n*d*c
SS_xx = np.sum(a*a) - n*c*c
plt.plot(a,b,'g')
plt.scatter(c2,d2, color = "green")
plt.show()