# Math modules:
# math square root:
import math
print(math.sqrt(16))

# without math
n = int(input("Enter a number: "))
print(n**0.5)

# math power(x,y):
print(math.pow(5,2))
# without math:
print(5**2)

# math floor:
print(math.floor(750.5))
# without math:
n = float(input("Enter a number: "))
print(n//1)

# math ceil:
print(math.ceil(35.6))

# math fabs:
print(math.fabs(-20))
# logic:
print(-20*-1)

# math factorial:
print(math.factorial(5))

# logic
fact = 1
n = int(input("Enter a number: "))
for i in range(n,0,-1):
    fact*=i
print(fact)    

# math gcd:
print(math.gcd(15,2))

# without math module:
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
gcd = 1
if a<b:
    smaller = a
else:
    smaller = b
for i in range(1,smaller+1):
    if a % i == 0 and b % i == 0:
        gcd = i
print(f'GCD of {a} and {b} is {gcd}')                


# math lcm:
print(math.lcm(2,8))