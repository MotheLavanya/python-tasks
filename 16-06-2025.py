# # 1. Take the list, take the sub list from the list and replace that sublist with sum of the sublist 
# list_a = list(input("Enter values"))
# print(list_a)
# sum = 0
# for i in list_a:
#     sum+=int(i) 
# start= int(input("Enter a number: "))
# end = int(input("Enter a number: "))
# list_a[start:end] = [sum]
# print(list_a)

list_a = list(input("Enter a elements: "))
print(list_a)
start= int(input("Enter a number: "))
end = int(input("Enter a number: "))
v = list_a[start:end]
print(v)
sum = 0
for i in v:
    sum+=int(i)
print(sum)
list_a[start:end] = [sum]
print(list_a)    

# 2. Find the second largest values in a list:
a = [10, 20, 4, 45, 99, 45]

# Initialize both to negative infinity
first = second = float('-inf')
for n in a:
    if n > first:
        second = first
        first = n
    elif n > second and n != first:
        second = n

print("Second largest is:", second)
