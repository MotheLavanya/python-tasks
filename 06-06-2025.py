# 1.slicing using positive indexing(strings):
string = "Learn Python Programming"
print(string[6:])  # begin form  
print(string[:12]) # end form
print(string[13:24])  # start and end positions
print(string[0:12:2])  # start,end,step

# 2.slicing using positive indexing(list):

list_a = [10,20,30,"item", True, 3.14, "list"]
print(list_a[4:]) # begin form 
print(list_a[:4]) # begin form 
print(list_a[1:6]) # start and end positions
print(list_a[1:7:3]) # start,end,step

# 3.slicing using positive indexing(tuple):
tuple_1 = (1,"a",2,"b",3,"c",2.15,False, "123456")
print(tuple_1[5:]) # begin form
print(tuple_1[:7]) # end form 
print(tuple_1[3:7]) # start and end positions
print(tuple_1[1:9:1]) # start,end,step

# Extract odd numbers using slicing:
string = "0123456789"
print(string[1::2])

list_b = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(list_b[1::2])

# Extract even numbers using slicing:
string_1 = "0123456789"
print(string_1[0::2])

list_c = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(list_c[0:11:2])


# slicing using negative indexing(strings):
name = "Tech Industry"
print(name[-1:]) # begin form
print(name[:-9]) # end form 
print(name[-1:-10:-1]) # start,end,step
print(name[-13:]) # start and end positions
print(name[-13:-9])
print(name[-6::-2])

# slicing using negative indexing(list):
lists = [1,2,3,"python", "Java","HTML", 8.9, True]
print(lists[-2:])
print(lists[:-3])
print(lists[-9:-1])
print(lists[-1::-2])

# slicing using negative indexing(tuple):
tuple_a = (1,2,"a","b",3,4,"c","d", "CSS",False, 9.6)
print(tuple_a[-9:])
print(tuple_a[:-5])
print(tuple_a[-1:-6:-1])
print(tuple_a[-9:-1])

text = "Welcome to Python"
# Expected: "Python"
print(text[-7::])