# Practce patterns
# double patterns:
# diamond:
rows = 5
for i in range(1,rows+1):
    res =""
    for space in range(rows-i):
        res+=" "
    for j in range(i):
        res+="*" + " "
    print(res)  
for i in range(rows-1,0,-1):
    res=""
    for sp in range(rows-i):
        res+=" "
    for j in range(i):
        res+="*" + " "
    print(res)                    

        # (or)

rows = 5
for i in range(1,2*rows):
    res = ""
    spaces = rows-i if i<= rows else i-rows 
    cols = i if i<= rows else (rows*2-i)
    for space in range(spaces):
        res+=" "
    for j in range(cols):
        res+="*" + " "
    print(res)               

#            (or)       

rows = 5
for i in range(1,2*rows):
    spaces = rows - i if i<= rows else i-rows
    cols = i if i<=rows else (rows*2)-i
    print((" "*spaces) + ("* "*cols))


# reverse  pattern:
rows = 5
for i in range(1,2*rows):
    spaces = i - 1 if i <= rows else 2*rows-i-1
    cols = rows - i +1 if i<= rows else i-rows+1
    print((" "*spaces) + ("* "*cols))

# diamond pattern using alphabets:
rows = 5
code = 97
for i in range(1,2*rows):
    res=""
    spaces = rows - i if i<= rows else i-rows
    cols = i if i<=rows else (rows*2)-i
    res+=(" " * spaces)
    for j in range(cols):
        res+= chr(code) + " "
        code+=1
    print(res)    
    