#  print numbers from 1 to n:
n = int(input("enter a number:"))
for i in range(1,n):
    print(i)
    

# print all even numbers between 1 to n:
n = int(input("Enter a number:"))
for i in range(1,n+1):
    if i %2 == 0:
        print(i)    

# print all odd numbers from 1 to n:
n = int(input("Enter a number:"))
for i in range(1,n+1):
    if i % 2 != 0:
        print(i)

# print character in a string "Python":
word = "Python"
for i in word:
    print(i)  

# print sum of numbers from 1 to 100:
sum = 0
for i in range(1,101):
    sum = sum + i
print(sum)    

# print multiplication table 5:
n = int(input("Enter a number:"))
for i in range(1,11):
    print(n,"*",i,"=",n*i)

# print all elements of a list using a loop:
list = ["apple","banana","cherry"]
for i in list:
    print(i)  

# print only vowels from string "education":
word = "education"
for i in word:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        print(i)    

# # count how many times "a" appers in a string "banana" using a loop:
fruit = "banana"
count = 0
for i in fruit:
    if i == "a":
        count = count + 1
print(count)    


# Print numbers from 10 to 1 using a loop (reverse order).

for i in range(10,0,-1):
    print(i)

# ask the user to enter a 5 number using a loop and print their sum:
n = int(input("Enter a number:"))
sum = 0
for i in range(n):
    sum = sum + i
print(sum)    

# (or)

total = 0
for i in range(5):
    num = int(input("Enter number: "))
    total += num
print("The sum of the 5 numbers is:" ,total)
