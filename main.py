import numpy as np
m=np.array([[1,2,3,4],[2,3,4,5],[3,4,5,6]])
mean_col = np.mean(m, axis=0)
mean_row = np.mean(m, axis=1)
mean = np.mean(m)
print(m)
print(int(mean_col))
print(mean_row)
print(mean)