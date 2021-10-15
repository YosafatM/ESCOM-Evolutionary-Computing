# Knapsack problem
# Section 1: Data definition
import numpy as np

v = (2, 3, 4, 5, 6)   # Values
w = (2, 4, 5, 5, 7)   # Weights
W = 9                 # Total weight of the Knapsack
N = len(w)            # Number of objects

m = np.zeros((N + 1, W + 1))

# Section 2: Dynamic programming
for row in range(1, N + 1):
    for col in range(1, W + 1):
        if w[row - 1] > col:
            m[row][col] = m[row - 1, col]
        else:
            m[row][col] = max(m[row - 1][col], m[row - 1][col - w[row - 1]] + v[row - 1])

# Section 3: Answer searching
indices = []
current = W

for row in range(N, 1, -1):
    for col in range(current, 1, -1):
        if m[row][col] != m[row - 1][col]:
            indices.append(row)
            current = col - w[row-1]
            break

# Section 4: Report
elements = [v[index-1] for index in indices]
weights = [w[index-1] for index in indices]
print(m)

print("\nAnswer report:")
print("Elements: ", elements)
print("Weights: ", weights)
