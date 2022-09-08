import numpy as np
import matplotlib.pyplot as plt
exp=np.array([16,12,18,4,3,10,5,12])
performance=np.array([8,8,9,6,6,8,7,83])
m,c=np.polyfit(exp,performance,1)
s=m*25+c
print(s)
plt.scatter(exp,performance)
plt.plot(exp,exp*m+c)
plt.show()


