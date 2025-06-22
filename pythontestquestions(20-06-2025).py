# Rotate a list by k positions to the right.
# Example:
# Input: lst = [1, 2, 3, 4, 5], k = 2
# Output: [4, 5, 1, 2, 3]

a = [1,2,3,4,5]
k = 2
print(a[len(a)-k:] + a[:len(a)-k])

# Remove all duplicates from a list without using set().
# Input: [1, 2, 3, 2, 1, 4, 5]
# Output: [1, 2, 3, 4, 5]
input = [1,2,3,2,1,4,5]
a = []
for i in input:
    if i not in a:
        a.append(i)
print(a)        

# Find all pairs in a list that sum up to a target.
# Input: lst = [2, 4, 3, 5, 7], target = 7
# Output: [(2, 5), (4, 3)]
def sum_pairs(v,target):
    pairs =[]
    for i in range(len(v)):
        for j in range(i+1,len(v)):
            if v[i] + v[j] == target:
                pairs.append((v[i],v[j]))
    return pairs
v = [2, 4, 3, 5, 7]    
target = 7
print(sum_pairs(v,target))       
    
# Flatten a 2D list without using built-in flatten functions.
# Input: [[1, 2], [3, 4], [5]]
# Output: [1, 2, 3, 4, 5]

def flatten_2d(lst_2d):
    flat = []
    for sublist in lst_2d:
        for item in sublist:
            flat.append(item)
    return flat
lst = [[1, 2], [3, 4], [5]]
print(flatten_2d(lst))

# Count the frequency of each element in a list and return a dictionary.
# Input: [1, 2, 2, 3, 1, 4, 2]
# Output: {1: 2, 2: 3, 3: 1, 4: 1}

lst = [1, 2, 2, 3, 1, 4, 2]
freq = {}
for item in lst:
    if item in freq:
        freq[item] += 1
    else:
        freq[item] = 1 
print(freq)

# Check if a string is a palindrome (ignoring spaces and case).
# Input: "A man a plan a canal Panama"
# Output: True

s = "A man a plan a canal Panama"
normalized = ""
for ch in s:
    if ch != ' ':
        if 'A' <= ch <= 'Z':
            normalized += chr(ord(ch) + 32) 
        else:
            normalized += ch
is_pal = True
length = len(normalized)
for i in range(length // 2):
    if normalized[i] != normalized[length - 1 - i]:
        is_pal = False
        break
print(is_pal) 


# Find the first non-repeating character in a string.
# Input: "aabbcdeff"
# Output: 'c'
def first_non_repeating(s):
    n = len(s)
    for i in range(n):
        unique = True
        for j in range(n):
            if i != j and s[i] == s[j]:
                unique = False
                break
        if unique:
            return s[i]
    return None  # or any sentinel value

print(first_non_repeating("aabbcdeff"))

# Remove all vowels from a string.
# Input: "Hello World"
# Output: "Hll Wrld"

input = "Hello World"
string = ""
vowels = "aeiouAEIOU"
for i in input:
    if i not in vowels:
        string+=i
print(string)        

# Count the number of words in a string without using .split().
# Input: "Python is great"
# Output: 3
def count_words_prev(s):
    prev = ' '
    count = 0
    for ch in s:
        if ch == ' ' and prev != ' ':
            count += 1
        prev = ch
    if prev != ' ':
        count += 1
    return count
print(count_words_prev("Python is great"))   

# Find the longest word in a sentence.
# Input: "The quick brown fox jumps over the lazy dog"
# Output: "jumps"

sentence = "The quick brown fox jumps over the lazy dog"
words = sentence.split()
longest_word = words[0]
max_length = len(words[0])

for word in words:
    if len(word) > max_length:
        max_length = len(word)
        longest_word = word

print(longest_word) 







  










       
    
