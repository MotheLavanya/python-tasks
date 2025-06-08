# 1. sum of odd num using functions:
def sum_odd_numbers(n,m):
    sum = 0
    for i in range(n,m):
        if i % 2 != 0:
            sum+= i
    return sum
n = int(input("Enter a Number: "))
m = int(input("Enter a Number: "))
num = sum_odd_numbers(n,m)
print(num)       

# 2.  sum of prime numbers using functions :
def sum_prime_numbers(n):
    sum = 0
    for i in range(2,n+1):
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            sum+=i
    return sum
n = int(input("Enter a Number: "))
num = sum_prime_numbers(n)
print(num) 
# sum = 0
# for i in range(2,20):
#     for j in range(2,i):
#         if i % j == 0:
#             break
#     else:
#         sum+=i
# print(sum)     

         