import numpy as np

# Step 1: Define the matrix A
A = np.array([[1, 2, 3],
              [0, 1, 4],
              [5, 6, 0]])

# Step 2: Calculate the inverse of matrix A
A_inv = np.linalg.inv(A)

# Step 3: Verify A * A_inv and A_inv * A are close to the identity matrix
identity_matrix = np.identity(3)

# Check A * A_inv
product_A_A_inv = np.dot(A, A_inv)

# Check A_inv * A
product_A_inv_A = np.dot(A_inv, A)

# Print the results
print("Matrix A:")
print(A)
print("\nInverse of A (A_inv):")
print(A_inv)
print("\nA * A_inv (should be close to identity matrix):")
print(product_A_A_inv)
print("\nA_inv * A (should be close to identity matrix):")
print(product_A_inv_A)

# Check if the results are close to the identity matrix
print("\nAre both A * A_inv and A_inv * A close to the identity matrix?")
print(np.allclose(product_A_A_inv, identity_matrix, atol=1e-10))  # Tolerance for floating-point comparison
print(np.allclose(product_A_inv_A, identity_matrix, atol=1e-10))  # Tolerance for floating-point comparison
