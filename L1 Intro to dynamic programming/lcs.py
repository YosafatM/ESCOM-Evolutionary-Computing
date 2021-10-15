import numpy as np

# Section 1: Data definition
X = 'ABACDEH'
Y = 'BDFTE'
m = len(X)
n = len(Y)
matrix = np.zeros((m, n))


# Section 2: Dynamic programming
def lcs(string_a, string_b, l_a, l_b) -> int:
    answer: int

    if l_a == 0 or l_b == 0:
        return 0
    elif string_a[l_a - 1] == string_b[l_b - 1]:
        answer = 1 + lcs(string_a, string_b, l_a - 1, l_b - 1)
    else:
        answer = max(lcs(string_a, string_b, l_a, l_b - 1), lcs(string_a, string_b, l_a - 1, l_b))

    matrix[l_a-1][l_b-1] = answer
    return answer


length = lcs(X, Y, m, n)

# Section 3: Answer search
print(matrix)

row = m-1
col = n-1
subsequence = []
while not (row == 0 or col == 0):
    if matrix[row-1][col] == matrix[row][col]:
        row -= 1
    elif matrix[row][col-1] == matrix[row][col]:
        col -= 1
    else:
        row -= 1
        col -= 1
        subsequence.append(X[row+1])

if col != 0 and row == 0:
    for letter in Y[0: col]:
        if X[row] == letter:
            subsequence.append(X[row])
            break
elif col == 0 and row != 0:
    for letter in Y[0: row]:
        if letter == Y[col]:
            subsequence.append(Y[col])
            break
else:
    if X[row] == Y[col]:
        subsequence.append(Y[col])

print('\n' + X)
print(Y)
print('Longest subsequence: ')
print(''.join(reversed(subsequence)))
