# #  l = 5200
#  o/p : 10 500 notes 1 200 notes

amount = 5200
notes = [500, 200]
for note in notes:
    count = amount // note
    amount = amount % note
    print(f"{count} x ₹{note} notes")

#  2. p = ["Python", "java", "c++"]   # print only python from the list using tuple comprehension
p = ["Python", "java", "c++"] 
res = (i for i in p)
print(next(res))


# 3. print prime numbers between 10 to 20 using tuple comprehension
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

primes_10_20 = tuple(x for x in range(10, 21) if is_prime(x))
print(primes_10_20) 


#  4. given a string "abcd" create a tuple of ASCII value of each character
string = "abcd"
for i in string:
    print(ord(i))
res= tuple(ord(i) for i in string )
print(res)

result = tuple(ord(i) for i in string)
print(result)


#  5. l= [1,2,3,4,5,6]       o/p: [[1,2],[3,4],[5,6]]
l= [1,2,3,4,5,6] 
emp = []
for i in range(0,len(l),2):
    emp.append(l[i:i+2])
print(emp)    


list_a = [l[i:i+2] for i in range(0,len(l),2)]
print(list_a)

