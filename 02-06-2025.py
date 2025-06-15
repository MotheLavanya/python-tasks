# 1. Write a program to print the sum of all even numbers between 1 and 100.
def even_sum(a,b):
    sum = 0
    for i in range(a,b+1):
        if i % 2 == 0:
            sum = sum + i
    return sum
a = even_sum(1,101)  
print(a)     
a = even_sum(100,200)
print(a)

# 2. Write a program that prints the first 10 powers of 2 using a loop
def power_of_2():
    for i in range(10):
        print(2**i)
power_of_2()        

# 3. Calculate the factorial of a number entered by the user.
def fact(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    return fact
n = int(input("Enter a number"))
print(fact(n))   

# 4. Print the reverse of a given number (e.g., input 1234 → output 4321).
def reverse_num(n):
    reverse = 0
    while n != 0:
        a = n % 10
        reverse = reverse * 10 + a
        n = n // 10
    return reverse
n = int(input("Enter a number"))
print(reverse_num(n)) 

# 5. Count the number of digits in a given integer using a loop.
def count_digit(n):
    digit = 0
    while n != 0:
        a = n % 10
        digit = digit + 1
        n = n // 10
    return digit
n = int(input("Enter a Number"))
print(count_digit(n))

# 6. Write a program that prints all numbers from 1 to 100 that are divisible by both 3 and 5
def num_3_and_5(a,b):
    for i in range(a,b+1):
        if (i % 3 == 0 and i % 5 == 0):
            print(i)      
num_3_and_5(1,100)

# 7. Without using multiplication, calculate a * b using addition and a loop.
def multiplication(n):
    s = 0
    for i in range(1,n+1):
        s+=2
    return s
n = int(input("Enter anumber"))
print(multiplication(n))    


# 8. Print the sum of digits of a number entered by the user (e.g., 123 → 1+2+3 = 6).
def sum_digits_number(n):
    reversed = 0
    while n != 0:
        a = n % 10
        reversed = reversed + a
        n = n//10
    return reversed
n = int(input("Enter a number: "))
print(sum_digits_number(n))
   

# 9. Write a loop to check if a number is a palindrome (number reads the same forwards and backwards).
def palindrome(n):
    reverse = 0
    while n > 0:
        a = n % 10
        reverse = reverse *10 + a
        n = n // 10
    return reverse
n = int(input("Enter a number"))
if palindrome(n) == n:
    print(f"{n} is a palindrome!")
else:
    print(f"{n} is not a palindrome.")

# 10. Write a program to find the highest digit in a given number.
def high_digit(num):
    max_digit = 0
    for i in num:
        digit = int(i)
        if digit > max_digit:
            max_digit = digit
    return max_digit
num = input("Enter a number: ")
print(high_digit(num))        

# 11. Write a program to check if a number is positive, negative, or zero.
def number(n):
    if n > 0:
        result = "Positive number"
    elif n < 0:
        result = "Negative number"
    else:
        result = "Zero"
    return result
n = int(input("enter a number: "))
print(number(n))    
           

# 12. Write a program that takes a number and prints whether it is divisible by 2, 3, both, or neither.
def divisible_number(n):
    if (n % 2 == 0 and n % 3 == 0):
        result = n,"is divisible by 2 and 3"
    elif (n % 2 == 0):
        result = n,"is divisible by 2"
    elif (n % 3 == 0):
        result = n,"is divisible by 3"
    else:
        result = n, "is not divisible by 2 and 3"    
    return result    
n = int(input("Enter a number: ")) 
print(divisible_number(n))

# 13. Check if a number is a three-digit number using conditionals.
def three_digit_num(n):
    if (100 <= n and n <= 999):
        print(n, "is a three digit number")
    else:
        print(n, "is a not a three digit number") 
n = int(input("Enter a number: "))
three_digit_num(n)      

# 14. Write a program to check whether a given number is a prime number.
n = int(input("Enter a number: "))
if n <= 1:
    is_prime = False
else:
    is_prime = True
    i = 2
    while i * i <= n:
        if n % i == 0:
            is_prime = False
            break
        i += 1
if is_prime:
    print(f"{n} is a prime number.")
else:
    print(f"{n} is not a prime number.")


# 15. Write a program to find the largest of three numbers entered by the user using nested if-else.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a > b:
    if a > c:
        largest = a
    else:
        largest = c
else:
    if b > c:
        largest = b
    else:
        largest = c
print("The largest number is:", largest)


# (or)
def largest_num(a,b,c):
    if a > b and a > c:
        result = a,"is largest number"
    elif b > a and b > c:
        result = b, "is largest number"
    else:
        result =  (c, "is largest number")
    return result    
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))     
print(largest_num(a,b,c))

           

# 16. Check if a year is a leap year or not.
def leap_year(n):
    if (n % 4 == 0 and n % 100 != 0) or (n%400 == 0):
        print(f"{n} is a Leap Year")
    else:
        print(f"{n} is Not a Leap Year")
n = int(input("Enter a year: "))
leap_year(n)        
# 17. Take an integer input and determine if it is even and greater than 50.
def even_greaterthan_50(n):
    if n % 2 == 0 and n > 50:
        result = n,"is a even and greater than 50"
    else:
        result = n, "is not satify the conditions"    
    return result
n = int(input("Enter a number"))
print(even_greaterthan_50(n))    

# 18. Write a program to classify a number as:
#  Less than 0: "Negative"
# * 0 to 9: "Single Digit"
# * 10 to 99: "Two Digits"
# * 100 and above: "Three or More Digits"

def number_classify(n):
    if n < 0:
        result = "Neagtive"
    elif n >= 0 and n <= 9:
        result = "Single Digit"
    elif n >= 10 and n <= 99:
        result = "Two Digits"
    else:
        result = "Three or More Digits" 
    return result   
n = int(input("Enter a number: "))
print(number_classify(n))


# 19. Write a program to check if the square of a number is greater than 1000, and if yes, print the square.
def square_1000(n):
    if n**2 > 1000:
        print(n)
    else:
        print("Square is not greater than 1000")
n = int(input("Enter a number: "))   
square_1000(n)         

# 20. Take two integers as input and determine if one is a factor of the other.
def factor(a,b):
    if b != 0 and a % b == 0:
        print(f"{b} is a factor of {a}")
    elif a != 0 and b % a == 0:
        print(f"{a} is a factor of {b}")
    else:
        print("Neither is a factor of the other")
a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))   
factor(a,b)     






                










            








