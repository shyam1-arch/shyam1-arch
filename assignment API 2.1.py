import numpy as np
import matplotlib.pyplot as plt

# Ensure using the appropriate backend for matplotlib
import matplotlib
matplotlib.use('TkAgg')  # Change the backend to 'TkAgg'

# Define the range of x values
x = np.linspace(-10, 10, 400)

# Define the equations of the lines
y1 = 2 * x + 1
y2 = 2 * x + 2
y3 = 2 * x + 3

# Plot the lines
plt.plot(x, y1, label='y = 2x + 1', color='blue')
plt.plot(x, y2, label='y = 2x + 2', color='green')
plt.plot(x, y3, label='y = 2x + 3', color='red')

# Add labels and title
plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of y = 2x + 1, y = 2x + 2, y = 2x + 3')

# Show a legend
plt.legend()

# Display the plot
plt.grid(True)
plt.show()

