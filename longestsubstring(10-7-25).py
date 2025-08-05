# Count the palindrome substrings in a given input:
word = input("Enter a word: ")
longest = ""
count = 0
i = 0
while i < len(word) and len(word[i::])>len(longest):
    temp =""
    for j in range(i,len(word)):
        temp+=word[j]
        if temp==temp[::-1] and len(temp)>len(longest):
            count+=1
            longest = temp
    i+=1
print(f'longest substring is {longest}')
print(f'no.of substrings in a word is {count}')