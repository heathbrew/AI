from array import array
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
a=np.array([2,3,5,7,9])
b=np.array([4,5,7,10,15])
x = np.mean(a)
y = np.mean(b)
n= len(a)
numer = 0
denom = 0
for i in range(n):
 numer += (a[i] - x) * (b[i] - y)
 denom += (a[i] - x) ** 2
m = numer / denom
c = b - (m * x)
print(m)
c,d = np.polyfit(a,b,1)
plt.scatter(a,b)
plt.plot(a,a*c+d)
plt.show()