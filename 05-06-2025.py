# chaitanya----->aiaa
def name(n):
    s = ""
    b = "ai"
    for i in range(len(n)):
        if n[i] in b:
            s = s + n[i]
    return s
n = input("Enter a name")
print(name(n))        

 
# concate even positions in string chaitanya:
def string_name(n):
    b = ""
    for i in range(len(n)):
        if i % 2 == 0:
            b = b + n[i]
    return b
n = input("Enter a name")
print(string_name(n))        

# take two indexes and concate that part of indexes:
def str_name():
    for i in range(1,4):
        print(n[i],end="")
n = input("enter a name")
str_name()
        

    


