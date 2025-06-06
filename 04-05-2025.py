# find the length of string without using length method:
def len_string(n):
    count = 0
    for i in n:
        count = count + 1
    return count
n = input("enter a word")
print(len_string(n))    

# word = input("enter a string")
# count = 0
# for i in word:
#     count = count + 1
# print(count)    

# find the counts of a's in a given input:
def count_a(n):
    count = 0
    for i in word:
        if i == "a":
            count = count + 1
    return count
word = input("Enter a word")
print(count_a(word))        


# item = input("enter a number")
# count = 0
# for i in item:
#     if i == "a":
#         count = count + 1
# print(count)      

# # reverse a string:
# rev_string = input("enter a word")
# reverse = ""
# for i in rev_string:
#     reverse = i + reverse 
# print(reverse)    

def reverse_string(n):
    reverse = ""
    for i in word:
        reverse = i + reverse
    return reverse
word = input("Enter a word")
item = reverse_string(word) 
print(item)  

# find no.of a,e,i,o,u in a string:
def fun_name(n):
    count = 0
    for i in word:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            count = count + 1
    return count        
word = input("Enter a string")
m = fun_name(word)
print(m)        


# (or)
def vowels_string(n):
    count = 0
    s = "aeiou"
    for i in n:
        if i in s:
            count = count + 1
    return count
n = input("enter a string")
print(vowels_string(n))        

