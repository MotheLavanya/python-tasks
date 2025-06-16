# 1.Print first 10 natural numbers
def prime_numbers(n):
    for i in range(1,n+1):
        print(i) 
n = int(input("Enter a number: "))
prime_numbers(n)    
    
# 2. Print numbers divisible by 7 and multiples of 5 within a range
def num_7_5(a,b):
    for i in range(a,b):
        if (i % 7 == 0 and i % 5 == 0):
            print(i)
a = int(input("Enter a Number: "))
b = int(input("Enter a number: "))             
num_7_5(a,b)

# 3.print number is divisible by 3 fizz and divisble by 6 buzz and both number fizzbuzz:
def fizz_buzz(n):
    if n % 3 == 0 and n % 7 == 0:
        result = "FizzBuzz"
    elif n % 3 == 0:
        result = "Fizz"
    elif n % 7 == 0:
        result = "Buzz"
    else:
        result = n
    return result
n = int(input("Enter a number: "))  
print(fizz_buzz(n))                  

# 4.Iterate over a list, printing each ×10
def numbers(n):
    for i in n:
        print(i * 10)
n = [1,3,5,2,4,7,6,9,8,4]
numbers(n)

# 5.Print multiplication table ffrom 1 to n (like 5 x 1 = 5, ... 5 x 10 = 50).
def multiplication_table(n):
    for i in range(1,n+1):
        for j in range(1,11):
            print(i,"*",j,"=",i*j)
n = int(input("Enter a number: "))
multiplication_table(n) 

# 6. Print the characters of the string "Python" one by one using a loop.
def characters(word):
    for i in word:
        print(i)
word = input("Enter a word: ")
characters(word)          
# 7.Print all elements of a list using a loop. List: ["apple", "banana", "cherry"]
def elements(text):
    for i in text:
        print(i)
text = list(input("Enter a valiues: "))
elements(text)    

# 8. Print only the vowels from the string "education" using a loop.
def vowels(word):
    for i in word:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            print(i)
word = input("Enter a word")            
vowels(word)          

# 9.Count how many times the letter 'a' appears in the string "banana" using a loop.
def count_a(word):
    count = 0
    for i in word:
        if i == "a":
            count+=1
    return count
word = input("Enter a string")
print(count_a(word))        


# 10.Print numbers from 10 to 1 using a loop (reverse order).
def reverse_number():
    for i in range(10,0,-1):
        print(i)
reverse_number()        

# 11.Ask the user to enter 5 numbers using a loop and print their sum.
def number():   
    total = 0
    for i in range(5):
        num = int(input("Enter number: "))
        total += num
    print("The sum of the 5 numbers is:" ,total)
number()    

# 12. greater value of 3 numbers
def greatest_two(a,b,c):
    if a > b and a > c:
        result = "a is greatest number"
    elif b > c and b > a:
        result = "b is greatest number"
    else:
        result = "c is greatest number"
    return result    
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))   
c = int(input("Enter a number: ")) 
print(greatest_two(a,b,c))   
              
#13. greater value of 2 numbers:
def greater_2(a,b):
    if a > b:
        result = "a is greater number"
    else:
        result = "b is greater number" 
    return result   
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
print(greater_2(a,b))

# 14. Calculate the factorial of a number entered by the user.
def factorial(n):
    fact= 1
    for i in range(1,n+1):
        fact*=i
    return fact
n = int(input("Enter a number: ")) 
print(factorial(n))   

# 15.Print the reverse of a given number (e.g., input 1234 → output 4321).
def reverse_num(n):
    revrese = 0
    i = 1
    while n != 0:
        a = n % 10
        revrese = revrese * 10 + a
        n = n // 10
        i+=1
    return revrese
n = int(input("Enter a number: "))
print(reverse_num(n))    

# 16.Check whether a number is an Armstrong number or not (3-digit):
def armstrong_number(n):
    length = len(n)
    total = 0
    for i in n:
        total = total + (int(i)**length)
    return total
n = input("Enter a number: ")         
if n == armstrong_number(n):
    print(f'{n} is a armstrong number')
else:
    print(f'{n} is not a armstrong number')    

# 17.Write a program that prints all numbers from 1 to 100 that are divisible by both 3 and 5:
def divisible_by_3_5():
    for i in range(1,101):
        if (i % 3 == 0) and (i % 5 == 0):
            print(i)
divisible_by_3_5()    

# 18.calculate the sum of first n natural numbers  
def sum_natural_numbers(n):
    sum =0
    for i in range(1,n+1):
        sum+=i
    return sum
n = int(input("Enter a number: "))
print(sum_natural_numbers(n))          

# 19.Print the ASCII value of each character in a string.
def ascii_character(word):
    for i in word:
        print(i,ord(i))
word = input("Enter a string: ")
ascii_character(word)      

# 20. # Convert a lowercase character to uppercase using ASCII values in a loop.
# word = "LAvanya"
# result = ""
# for i in word:
#     if ord("a") <= ord(i) <= ord("z"):
#         result+= chr(ord(i) - 32)
#     else:
#         result+=i
# print(result)      

def lower_upper(word):
    result = ""
    for i in word:
        if ord("a") <= ord(i) <= ord("z"):
            result+=chr(ord(i) - 32)
        else:
            result+=i
    return result
word = input("Enter a word")    
print(lower_upper(word))    


