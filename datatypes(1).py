
# create variables of different types
name = "John"
age = 25
height = 5.9
is_student = True
print(type(name))
print(type(age))
print(type(height))
print(type(is_student))

# Change value and Type
a = 30
print(type(a))
a = "fruit"
print(type(a))

# Guess the Type
a = 10
b = 3.14
c = "hello"
d = True
print(type(a))
print(type(b))
print(type(c))
print(type(d))

list_a = [10,3.14,"hello",True]
print(type(list_a))

# variable Naming Practice
name = "Lavanya"
marks = 85
is_passed = True

print(name)
print(marks)
print(is_passed)

# Identify Errors:
# ...1name = "Alice" # variable should not start with number
# my-age = 20 # variable should not contain special characters
# print(Name) # variable name is not defined....

# Correct Way:
name_1 = "Alice"
my_age = 20
print(name_1)
print(my_age)

#simple story with Variables:
name = "10000Coders"
good ="good"
print(name, "is a", good, "institute")

# swap two numbers:
a = 5
b = 6
a = a+b
b = a - b
a = a - b
print(a,b)

# (or)

a = 2
b = 3
a,b = b,a
print(a,b)