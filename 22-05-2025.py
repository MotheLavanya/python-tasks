# Q1 : Multiplication Table (1 to 10)
# Write a Python program using nested loops to print the multiplication tables from 1 to 10.
def multiplication():
    for i in range(1,n+1):
        for j in range(1,11):
            print(i,"*",j,"=",i*j)
n = int(input("Enter a number: "))
multiplication()            

# Q2. Count Prime Numbers in a Range (1 to 100)
# Using nested loops, count how many prime numbers exist between 1 and 100.
def prime_number():
    for i in range(2,101):
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            print(i)
prime_number()          

# Q3. Print All Pairs of Numbers (1 to n) Where Sum is Even
# Ask the user to enter a number n. Using nested loops, print all pairs (i, j) from 1 to n where the sum i + j is even.
# Example for n = 3:
# (1,1)
# (1,3)
# (2,2)
# (3,1)
# (3,3)
def all_pairs(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if (i+j)%2 == 0:
                print(i,j)
n = int(input("Enter a number: "))
all_pairs(n)              

# Q4. Count Total Factors of All Numbers from 1 to n
# Ask the user to enter a number n. Use nested loops to find how many total factors (divisors) exist for all numbers from 1 to n.
# Example for n = 4
# 1 → 1
# 2 → 1, 2
# 3 → 1, 3
# 4 → 1, 2, 4
# Total = 8 factors
def count_factors(n):
    count = 0
    for i in range(1,n):
        for j in range(1,i+1):
            if i % j == 0:
                count+=1
    return count
n = int(input("Enter a number: "))
print(count_factors(n))

# Q5. Print All Pythagorean Triplets with Values ≤ n
# Ask the user to enter n. Find and print all  Pythagorean triplets (a, b, c) such that a² + b² = c² and a, b, c ≤ n.
# Example for n = 20:
# (3, 4, 5)
# (5, 12, 13)
# (6, 8, 10)
# (8, 15, 17)
def pythagorea_triplets(n):
    for i in range(1,n+1):
        for j in range(i,n+1):
            for k in range(j,n+1):
                if (i**2 + j **2 == k**2) and k < n:
                    return i,j,k
n = int(input("Enter a number: "))
print(pythagorea_triplets(n))               



