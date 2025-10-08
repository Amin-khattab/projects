import numpy as np
import matplotlib.pyplot as plt

# Step 1: Create data (x, y)
x = np.array([1, 2, 3, 4, 5])
y = np.array([3, 4, 2, 5, 6])

x_mean =np.mean(x)
y_mean =np.mean(y)

w1 = np.sum((x - x_mean)*(y - y_mean) / np.sum((x - x_mean)**2))
w0 = y_mean - w1 * x_mean

y_pred = w0 + w1 * x

print(y_pred)

plt.scatter(x,y)
plt.plot(x,y_pred,color = 'red')
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()
