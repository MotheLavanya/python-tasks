# 1.Print a specific part of a string without using slicing:
n = input("Enter a String: ")
a = int(input("Enter a number"))
b = int(input("Enter a number"))
slicing = " "
for i in range(a,b):
    slicing = slicing + n[i]
print(slicing)    

# # 2. Print the string to replace "is" with "si" without using replace method:

s = "hi this is ram and is raj"
parts = s.split("is")  # splits on every "is"
result = "si".join(parts)
print(result)

# 3.   
input_str = "chai_yany_raj"
result = ""
i = 0
while i < len(input_str):
    if input_str[i] == "_":
        i += 1
        result += input_str[i].upper()
    else:
        result += input_str[i]
    i += 1
print(result)  

