# Rotate a string k no.of times from left to right and right to left
# right rotation
v = input("Enter a string: ")
k = int(input("Enter a number: "))
print(v[len(v)-k:] + v[:len(v)-k])

# left rotation
print(v[k:] + v[:k])

# (Or)
# left rotation
v = "python"
n = 3
i = 0
left_text = v
while i < n:
    left_text = left_text[1:] + left_text[0]
    print(left_text)
    i+=1    

# right rotation

result = "python"
i = 0
n = 4
while i < n:
    result = result[-1] + result[:-1]
    print(result)
    i+=1    

