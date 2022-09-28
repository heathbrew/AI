from sklearn.metrics import mean_squared_error
from math import sqrt
from sklearn.metrics import r2_score
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
a = pd.read_csv(r"Position_Salaries.csv")
print(a)
s = a["Salary"]
ss = a["Level"]
plt.scatter(s,ss,color="black")
plt.plot(s,ss,color="c")
s2 = np.array(s)
sw = np.array(ss)
c , d = np.polyfit(s2,sw,1)
plt.plot(s2,s2*c+d,color = 'black')
plt.show()
m = sqrt(mean_squared_error(s2, sw)) 
print("RMSE:",m)
m2 = r2_score(s2,sw)
print("R2 SCORE:",m2)