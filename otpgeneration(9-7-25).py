import random as p
n = int(input("Enter a number: "))
s = ""
for i in range(n):
    a = p.randint(1,9)
    s+=str(a)
print(s)    