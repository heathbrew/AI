import numpy as np
import matplotlib.pyplot as plt
x=np.array([8,3,2,10,11,3,6,5])
y=np.array([4,12,1,12,9,4,6,1])
m,c=np.polyfit(x,y,1)
plt.scatter(x,y)
plt.plot(x,x*m+c)
plt.show()

