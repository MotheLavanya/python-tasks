#  Take a string print all upper case letters at first and lower case letters at last  without using method:
n = input("Enter a string")
upper = ""
lower = ""
for i in n:
    if ord(i) >= 65 and ord(i) <= 90:
        upper+=i
    else:
        lower+=i
print(upper+lower)            