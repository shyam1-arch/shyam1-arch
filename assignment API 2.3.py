import matplotlib
matplotlib.use('TkAgg')  # Change the backend to TkAgg

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load CSV file into a Pandas DataFrame
data = pd.read_csv('weight-height.csv')

# Step 2: Extract lengths and weights into numpy arrays
length_in = data['Height'].to_numpy()  # Assuming 'Height' column contains lengths in inches
weight_lb = data['Weight'].to_numpy()  # Assuming 'Weight' column contains weights in pounds

# Step 3: Convert lengths from inches to centimeters and weights from pounds to kilograms
length_cm = length_in * 2.54  # Convert inches to centimeters
weight_kg = weight_lb * 0.453592  # Convert pounds to kilograms

# Step 4: Calculate the means of the lengths and weights
mean_length = np.mean(length_cm)
mean_weight = np.mean(weight_kg)

# Print the means
print(f"Mean length (cm): {mean_length:.2f}")
print(f"Mean weight (kg): {mean_weight:.2f}")

# Step 5: Draw a histogram of the lengths
plt.hist(length_cm, bins=20, edgecolor='black', alpha=0.7)
plt.title('Histogram of Lengths (in cm)')
plt.xlabel('Length (cm)')
plt.ylabel('Frequency')
plt.show()
