# Todays Python tasks

# Task 1: Square All Numbers Using map()
# Given a list of numbers, create a new list containing their squares using map().
# Input: [1, 2, 3, 4, 5]
# Expected Output: [1, 4, 9, 16, 25]
list_a = [1, 2, 3, 4, 5]
print(list(map(lambda x : x**2,list_a)))

# Task 2: Filter Even Numbers Using filter()
# Given a list of numbers, filter out only the even numbers using filter().
# Input: [10, 15, 22, 33, 40]
# Expected Output: [10, 22, 40]
list_b = [10, 15, 22, 33, 40] 
print(list(filter(lambda y : y%2==0, list_b)))

# Task 3: Convert All Strings to Uppercase Using map()
# Given a list of lowercase words, convert all words to uppercase using map().
# Input: ['apple', 'banana', 'cherry']
# Expected Output: ['APPLE', 'BANANA', 'CHERRY']
elements = ['apple', 'banana', 'cherry']
print(list(map(lambda i : i.upper(),elements)))

# Task 4: Filter Words Starting with 'a' Using filter()
# Given a list of words, filter out only the words that start with the letter 'a'.
# Input: ['apple', 'banana', 'apricot', 'grape', 'avocado']
# Expected Output: ['apple', 'apricot', 'avocado']
fruits = ['apple', 'banana', 'apricot', 'grape', 'avocado']
print(list(filter(lambda j : j[0]=="a",fruits)))

# Task 5: Find the Length of Each Word Using map()
# Given a list of words, find the length of each word using map().
# Input: ['hello', 'world', 'python']
# Expected Output: [5, 5, 6]
words = ['hello', 'world', 'python']
print(list(map(lambda a : len(a),words)))

# Task 6: Filter Out Numbers Less Than 10
# Given a list of numbers, filter out numbers that are less than 10 using filter().
# Input: [4, 11, 7, 20, 3, 15]
# Expected Output: [11, 20, 15]
inputs = [4, 11, 7, 20, 3, 15]
print(list(filter(lambda b : b>10, inputs)))

# Task 7: Double Each Number Using map()
# Given a list of numbers, double each number using map().
# Input: [1, 2, 3, 4]
# Expected Output: [2, 4, 6, 8]
values = [1, 2, 3, 4]
print(list(map(lambda c : c+c, values)))

# Task 8: Filter Names Longer Than 5 Characters
# Given a list of names, filter out names longer than 5 characters using filter().
# Input: ['John', 'Elizabeth', 'Sam', 'Chris', 'Amanda']
# Expected Output: ['Elizabeth', 'Amanda']
names =  ['John', 'Elizabeth', 'Sam', 'Chris', 'Amanda']
print(list(filter(lambda v : len(v)> 5, names)))


# Task 9: Add Exclamation Mark to Each Word
# Given a list of words, add an exclamation mark at the end of each word using map().
# Input: ['python', 'java', 'ruby']
# Expected Output: ['python!', 'java!', 'ruby!']
list_c =  ['python', 'java', 'ruby']
print(list(map(lambda n : n+"!",list_c )))

# Task 10: Filter Numbers That Are Multiples of 3
# Given a list of numbers, filter out only those that are multiples of 3 using filter().
# Input: [3, 4, 9, 10, 15, 17, 21]
# Expected Output: [3, 9, 15, 21]
list_b = [3, 4, 9, 10, 15, 17, 21]
print(list(filter(lambda d : d % 3 == 0,list_b ))) 