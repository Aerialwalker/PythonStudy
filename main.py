import numpy as np

x = np.array([[15, 20], [20, 21]])
print(x[0][1])

x = x.flatten()
print(x)
print(x[np.array([0, 2, 3])])

print([x > 15])
print(x[x > 15])
