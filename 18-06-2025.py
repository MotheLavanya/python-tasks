# 1. Take two dimensional array (square matrix) print diagnol values in list
v= [
[1,3,6],
[4,7,5],
[6,4,9]
]
for i in range(len(v)):
    print(v[i][i])
print()    

# 2. Print anti diagonal values in list:

v= [
[1,3,6],
[4,7,5],
[6,4,9]
]
for i in range(len(v)):
    print(v[i][len(v)-i-1])