#  H pattern:
rows = int(input("Enter a number: "))
for i in range(1,rows+1):
    res= " "
    for j in range(1,rows+1):
        if j == 1 or j == rows or i==(rows//2)+1:
            res+="*" + " "
        else:
            res+=" "+ " " 
    print(res)           

# N pattern:
rows = int(input("Enter a number: "))
for i in range(1,rows+1):
    res = " "
    for j in range(1,rows+1):
        if j == 1 or j == rows or i==j:
            res+="*" + " "
        else:
            res+= " " + " "
    print(res)         
# E pattern:
rows = int(input("Enter a number: "))
for i in range(1,rows+1):
    res = " "
    for j in range(1,rows+1):
        if i ==1 or j==1 or i==rows or i==(rows//2)+1:
            res+= "*" + " "
        else:
            res+=" " + " "
    print(res)     