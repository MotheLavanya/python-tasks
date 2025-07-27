# Z pattern:
rows = int(input("Enter a number: "))
for i in range(1,rows+1):
    res = ""
    for j in range(1,rows+1):
        if i == 1 or i == rows or i+j==rows+1:
            res+="*"+" "
        else:
            res+=" " + " "    
    print(res)  

# * * * * * 
#       *   
#     *     
#   *       
# * * * * *    
       
#  Y pattern:
rows = int(input("Enter a number: "))
for i in range(rows):
    for j in range(rows):
        if (i <= rows // 2 and (j == i or j == rows - i - 1)) or (i > rows // 2 and j == rows // 2):
            print("*", end="")
        else:
            print(" ", end="")
    print()

# *     *
#  *   *
#   * *
#    *
#    *
#    *
#    *    

# M pattern:

rows = int(input("Enter a number: "))

for i in range(rows):
    for j in range(rows):
        if j == 0 or j == rows - 1 or (i == j and j <= rows // 2) or (i + j == rows - 1 and j >= rows // 2):
            print("*", end="")
        else:
            print(" ", end="")
    print()

# *   *
# ** **
# * * *
# *   *
# *   *    