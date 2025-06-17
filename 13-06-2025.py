# Even or Odd Checker:
# Take an integer as input and print whether it's even or odd.
def even_odd(v):
    for i in v:
        if int(i) % 2 == 0:
            print("Even Number")
        else:
            print("Odd Number")  
v = list(input("Enter a values:"))  
even_odd(v)                        

# Sum of Digits:
# Given a number, find the sum of its digits (e.g., 123 ➝ 6).
v = [1,2,3,5,8,9,4]
sum = 0
for i in range(len(v)):
    sum+=v[i]
print(sum)    

# Count Vowels in a String:
# Input a string and count how many vowels it contains.
word = input("Enter a string")
vowels = "aeiouAEIOU"
count = 0
for i in word:
    if i in vowels:
        count+=1
print(count)

# Check Palindrome:
# Check if a given string or number is a palindrome (same forward and backward).
word = input("Enter a string: ")
reverse = ""
for i in word:
    reverse = i + reverse
if reverse == word:
    print("Palindrome")
else:
    print("Not a palindrome")      

# Find Maximum in a List:
# Given a list of numbers, find and print the maximum number.
def max_list(v):
    max_num = v[0]
    for i in v:
        if max_num < i:
            max_num = i
    return max_num
v = list(input("Enter a number: "))
print(max_list(v))        


