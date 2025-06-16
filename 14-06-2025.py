# 1.Reverse a String Without Using [::-1]:
# Reverse a string using a loop or recursion
def palindrome(n):
    result = ""
    for i in n:
        result = i + result
    return result
n = input("Enter a string")
print(palindrome(n))    

# or

def palindrome(v):
    left = 0
    right = len(v) - 1
    while left < right:
        if v[left] != v[right]:
            print("Not a Palindrome")
            break 
        left+=1
        right-=1
    else:
        print("Palindrome") 
v = input("Enter a number :")
palindrome(v)           



# # 2.Count Frequency of an Element in a List:
# # Input a list and an element, count how many times the element appears.
# n = list(input("Enter Elements"))

def count_elements(num,n):
    count = 0
    for i in num:
        if int(i) == n:
            count+=1
    return count
num = list(input("Enter a elements: "))
n = int(input("Enter a number: "))
print(count_elements(num,n))        

#3. Print First N Prime Numbers:
# Take N as input and print the first N prime numbers.
n = int(input("Enter a number"))
for i in range(2,n+1):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        print(i)   

#4. Remove Duplicates from a List:
# Given a list, return a new list without duplicates (maintain order).
# n = list(input("Enter a values"))
# print(n)
# result  = []
# for i in n:
#     if i not in result:
#         result.append(i)
# print(result)        

def duplictes(n):
    result = []
    for i in n:
        if i not in result:
            result.append(i)
    return result
n = list(input("Enter a values: "))
print(duplictes(n))


#5. For numbers from 1 to N, print:
# “Fizz” if divisible by 3
# “Buzz” if divisible by 5
# “FizzBuzz” if divisible by both
# Else print the number itself.
              

def number_divisible(n):
    for i in range(1,n+1):
        if i % 3 == 0 and i % 5 == 0:
            result = "FizzBuzz"
        elif i % 3 == 0:
            result = "Fuzz"
        elif i % 5 == 0:
            result = "Buzz"
        else:
            result = n
    return result
n = int(input("Enter a number: "))
print(number_divisible(n))                    




