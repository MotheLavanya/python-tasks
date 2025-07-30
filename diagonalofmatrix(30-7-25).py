# diagonal of the square matrix:
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
for i in range(len(matrix)):
    print(matrix[i][i])
print()
# output:
# 1
# 5
# 9


# Anti-diagonal of the square matrix:    
for i in range(len(matrix)):
    print(matrix[i][len(matrix)-i-1])

# output:
# 3
# 5
# 7