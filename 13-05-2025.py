# 1.Even or Odd Number
n = int(input("Enter a number"))
if n % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")    

# 2. Positive, Negative, or Zero  
n = int(input("Enter a number"))
if n > 0:
    print("Positive Number")
elif n < 0:
    print("Negative Number")
else:
    print("Zero")          

# 3. Leap Year Checker
n = int(input("Enter a year"))
if (n % 4 == 0 and n % 100 !=0) or (n % 400 == 0):
    print(n, "is a Leap Year")
else:
    print(n, "is Not a Leap Year")             



# 4.Check if a number is divisible by both 5 and 11.
n = int(input("Enter a Number: "))
if (n % 5 == 0 and n % 11 == 0):
    print(n, "is divisible by both 5 and 11")
else:
    print(n, "not divisible by 5 and 11")    


# 5. Take an integer input and determine if it is even and greater than 50.
n = int(input("Enter a Number: "))
if (n % 2 == 0 and n > 50):
    print(n, "is a even and greater than 50")
else:
    print(n, "is not a even and not greater than 50")   

# 6.  Write a program to find the largest of three numbers entered by the user using conditionals statements.
a = int(input("Enter a number"))
b = int(input("Enter a number"))
c = int(input("Enter a number"))
if a > b and a > c:
    result = "a is greater"
elif a < b and c < b:
    result = "b is greater"
else:
    result = "c is greater"        
print(result)    