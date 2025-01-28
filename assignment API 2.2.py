import matplotlib
matplotlib.use('TkAgg')  # Set a compatible backend for rendering

import numpy as np
import matplotlib.pyplot as plt

# Create numpy vectors x and y
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
y = np.array([-0.57, -2.57, -4.80, -7.36, -8.78, -10.52, -12.85, -14.69, -16.78])

# Create a scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(x, y, marker='+', color='black')
plt.title("Scatter Plot of Points (x, y)")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)

# Display the plot
plt.show()
