# 1.Print all numbers from 1 to N using a loop.
n = int(input("Enter a Number: "))
for i in range(1,n+1):
    print(i)

# 2.Print all even numbers from 1 to N.
n = int(input("Enter a Number: "))
for i in range(1,n+1):
    if i % 2 == 0:
        print(i)

# 3.Print all odd numbers from 1 to N.
n = int(input("Enter a Number: "))
for i in range(1,n+1):
    if i % 2 != 0:
        print(i)

# 4.Calculate the sum of the first N natural numbers.
n = int(input("Enter a Number: "))
sum = 0
for i in range(1,n+1):
    sum+=i
print(sum)    

# 5. Print the multiplication table of a given number up to 10.
n = int(input("Enter a Number: "))
for i in range(1,11):
    print(n,"*",i,"=",n*i)

# 6. Count the number of digits in a given number.

n = int(input("Enter a number: "))
count = 0
while n != 0:
    rev = n % 10
    sum = sum + 1
    n//=10
print(sum) 

# 7. Reverse a given integer number.
n = int(input("Enter a Number: "))
revrese = 0
while n != 0:
    a = n % 10
    revrese = revrese * 10 + a
    n =  n // 10
print(revrese)    

# 8.Check whether a number is a palindrome or not.
n = int(input("Enter a number: "))
revrese = 0
while n!=0:
    a = n % 10
    revrese = revrese + a
    n = n//10
print(revrese)    

# 9.Check whether a number is a prime number.
n = int(input("Enter a Number: "))
count = 0
for i in range(1,n+1):
    if n % i == 0:
        count = count + 1
if count == 2:
    print(n, "is a prime number")
else:
    print(n,"is not a prime number")    

# 10. Print all prime numbers between 1 and N.
n = int(input("Enter a number: "))
for i in range(2,n+1):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        print(i)    
 
# 11.Find the factorial of a number using a loop.
n = int(input("Enter a number: "))
fact = 1
for i in range(1,n+1):
    fact*=i
print(fact) 

# 12. Calculate a raised to the power b using a loop (without using **).
base = 2
expo = 3
result = 1
for i in range(3):
    result = result * base
print(result)    

# 13. Calculate the sum of digits of a given number.
n = int(input("Enter a number: "))
sum = 0
while n != 0:
    rev = n % 10
    sum = sum + rev
    n//=10
print(sum)   
# (or)
n = int(input("Enter a number")) 
a = str(abs(n))   # abs(absolute value----any negative value converted into positive value) and str(convert integer to string then iterate)              
total = 0
for i in a:
    total = total + int(i)
print(total)    

# 14. Check whether a number is an Armstrong number or not (3-digit).
n = int(input("Enter a number"))
temp = n
total = 0
while temp > 0:
    a = temp % 10
    total = total+ a**3
    temp//=10
if total == n:
    print(n, "is an armstrong number")
else:
    print(n, "is a not an armstrong number")

                #(or)

n = int(input("Enter a 3‑digit number: "))
temp = n
total = 0
for _ in range(3):
    digit = temp % 10
    total = total + digit**3
    temp//=10
if total == n:
    print("armstrong number")
else:
    print("not a armstrong number")  
#    
                #(or)

n = input("Enter a number: ")
length = len(n)
total = 0
for i in n:
    total = total + (int(i)**length)
if total == int(n):
    print("armstrong number")
else:
    print("Not a armstrong number ")           

# 15.Find the largest digit in a given number.
n = input()
max_digit = 0
for i in n:
    digit = int(i)
    if digit > max_digit:
        max_digit = digit
print(max_digit)   

# 16. Find the smallest digit in a given number.
n = input("Enter a number")
min_digit = 9
for i in n:
    digit = int(i)
    if digit < min_digit:
        min_digit = digit
print(min_digit)
 

# # 17.Count how many times a given digit appears in a number.
n = input("Enter a number: ")
x = input("enter a number")
count = 0
for i in n:
    if i == x:
        count = count + 1
print(count)        

# 18.Print the ASCII value of each character in a string.
text = input("Enter a string: ")
for i in text:
    print(ord(i))

# # 19.Count the number of vowels in a string using a loop.
n = input("Enter a string")
a = "aeiou"
count = 0
for i in n:
    if i in a:
        count = count + 1
print(count)        

# # 20. Print characters in a string one by one using a loop.
n = input("enter a word")
for i in n:
    print(i)

# 21. Print a pattern of stars using loops (e.g., triangle pattern).
n = int(input("Enter a number: "))
for i in range(1,n+1):
    print("* " * i,)

# 22.Convert a lowercase character to uppercase using ASCII values in a loop.
text = input("Enter text: ")
# Convert each character using its index
for i in range(len(text)):
    ch = text[i]
    ascii_val = ord(ch)
    if 97 <= ascii_val <= 122:  # 'a'–'z'
        # Convert to uppercase by subtracting 32
        new_ch = chr(ascii_val - 32)
        # Replace character in the string
        text = text[:i] + new_ch + text[i+1:]
print("\nUppercase:", text)


# 23.Check if a string is a palindrome without using slicing or reversed.
text = input("Enter a string: ")
is_palindrome = True

for i in range(len(text) // 2):
    if text[i] != text[len(text) - i - 1]:
        is_palindrome = False
        break

if is_palindrome:
    print("Yes, it's a palindrome")
else:
    print("No, it's not a palindrome")

 
# 24.Print the square of each number from 1 to N using a loop.
n = int(input("Enter a number: "))
for i in range(1,n+1):
    print(i**2)

# 25. Find the GCD (Greatest Common Divisor) of two numbers using a loop.
# Python program to find the GCD using a for loop
a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))

# Work with absolute values in case of negatives
a = abs(a)
b = abs(b)

# Initialize GCD variable
gcd = 1

# Determine smaller number for loop limit
if a < b:
    smaller = a
else:
    smaller = b

# Check every integer from 1 to smaller
for i in range(1, smaller + 1):
    if a % i == 0 and b % i == 0:
        gcd = i  # Update GCD when both are divisible

# Print the result
print(f"GCD of {a} and {b} is {gcd}")
