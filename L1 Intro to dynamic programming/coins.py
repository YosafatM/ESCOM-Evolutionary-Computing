# Change making problem
import numpy as np
import pandas as pd

# Section 1: Data definition
d = [1, 2, 5]   # Denominations
N = 9           # Change
N_den = len(d)
m = np.zeros((N_den, N + 1))

for col in range(1, N + 1):
    m[0][col] = col

# Section 2: Dynamic Programming
for row in range(1, N_den):
    for col in range(1, N + 1):
        if d[row] > col:
            m[row][col] = m[row - 1][col]
        else:
            m[row][col] = min(m[row - 1][col], m[row][col - d[row]] + 1)

# Section 3: Answer searching
current = N
solution = [0] * N_den

for row in range(N_den-1, -1, -1):
    if row == 0:
        solution[row] = m[row][current]
        break

    while m[row][current] != m[row-1][current]:
        solution[row] += 1
        current = current - d[row]

# Section 4: Answer report
print(m)

dictionary = {"Den": d, "Quantity": solution}
dt = pd.DataFrame.from_dict(dictionary)
dt = dt.set_index(["Den"])
dt = dt.convert_dtypes(convert_integer=["Quantity"])
print("\nChange required:", N)
print(dt)
