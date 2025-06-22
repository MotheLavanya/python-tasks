# 1. Reverse the list without using methods 
v = [1,2,3,4,56,"items"]
revrese = v[::-1]
print(revrese)   
# (or)
def rev_insert(lst):
    result = []
    for x in lst:
        result.insert(0, x)
    return result
lst = [1,2,3,4,5,6]
print(rev_insert(lst))   

# 2. Sort the list without using methods.
lst = [76, 23, 45, 12, 54, 9]
for i in range(len(lst) - 1):
    min_idx = i
    for j in range(i + 1, len(lst)):
        if lst[j] < lst[min_idx]:
            min_idx = j
    lst[i], lst[min_idx] = lst[min_idx], lst[i]
print(lst)

# (or)
arr = [76, 23, 45, 12, 54, 9]
n = len(arr)
for i in range(n):
    for j in range(0,n-i-1):
        if arr[i] > arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]
print(arr)   


# 3. Remove duplicates in the list without using methods :
lst = ['cat', 'dog', 'cat', 'mouse', 'dog']
unique = []
for item in lst:
    if item not in unique:
        unique.append(item)
print(unique)



# 4.1) Print the largest value in every list and concate the list 
# Ex: [ [2,3,1], [4,5,3], [7,6,8] ] => o/p [3,5,8]
# 4.2) Sum of Every list
lists = [[2,3,1], [4,5,3], [7,6,8]]
result = []
for i in range(len(lists)):
    sub = lists[i]
    max_val = sub[0]
    for j in range(1, len(sub)):
        if sub[j] > max_val:
            max_val = sub[j]
    result.append(max_val)
print(result)

# 4.2) Sum of Every list
lists = [ [2,3,1], [4,5,3], [7,6,8] ]
result = []
for i in range(len(lists)):
    sub = lists[i]
    total = 0
    for j in range(len(sub)):
        total += sub[j]
    result.append(total)
print(result)
         
