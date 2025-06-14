# Solve the below problems using for loop
# 1) sum of odd numbers, from 1 to 10?:
n = int(input("Enter a number: "))
sum = 0
for i in range(1,n+1):
    if i % 2 != 0:
        sum+= i
print(sum)        

# 2) Sum of even numbers from 1 to 10?
n = int(input("Enter a number: "))
sum = 0
for i in range(1,n+1):
    if i % 2 == 0:
        sum+= i
print(sum)     

# 3) sum of numbers from I to 10?:
n = int(input("Enter a number: "))
sum = 0
for i in range(1,n+1):
    sum+=i
print(sum)    

# 4) Find the Greatest of two numbers:
m = int(input("Enter a number: "))
n = int(input("Enter a number: "))
for i in range(1):
    if m > n:
        print(m)
    else:
        print(n)  

# 5) Find the Greatest of three numbers:
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))
for i in range(1):
    if a > b and a > c:
        print(f"{a} is greatest number")
    elif b > a and b > c:
        print(f"{b} is a greatest number")
    else:
        print(f"{c} is greatest number")         
          
# 6) print 1 to 10 Prime numbers
for i in range(2,11):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        print(i)    

# 7) Find the Leap Year:
n = int(input("Enter a year"))
if (n % 4 == 0 and n % 100 != 0) or (n % 400 == 0):
    print(f"{n} is a Leap Year")
else:
    print(f"{n} is not a Lear Year")    