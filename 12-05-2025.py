# 5 operations on list:
list_a = [1,"a",2,"b",3,True,2.32,"string"]
list_a.append(4)
print(list_a)
list_a.insert(1,300)
print(list_a)
list_a.remove(2.32)
print(list_a)
list_a.pop()
print(list_a)
list_a.insert(2,"A")
print(list_a)
print(len(list_a))

# 5 operations on Tuple:
tuple_a = (1,2,3,8,10,60,20,10,40,80,60)
a = tuple_a.count(10)
print(a)
print(max(tuple_a))
print(min(tuple_a))
print(sum(tuple_a))
print(len(tuple_a))
b = (8,9)
c = (7,6)
print(b+c)

# 5 operations on set:
set_a = {1,3,5,7,9,11,13,15,17,19,21,"Python","HTML"}
set_b = {2,4,6,8,10,12,14,16,18,20,22,"Java","CSS",1,3,5,7}
set_a.add(23)
print(set_a)
set_b.add(24)
print(set_b)
set_a.update([1.3,2.6,3,"Django"])
print(set_a)
set_b.update(["JavaScript","SQL"])
print(set_b)
print(set_a | set_b)    # Union
print(set_a & set_b) # intersection
print(set_a.symmetric_difference(set_b))