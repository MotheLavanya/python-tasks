# Task1:  print 1 to 5 tables using loops 
for i in range(1,6):
    for j in range(1,11):
        print(i ,"*" ,j ,"=",i*j)
    print()    

# Tas2:#print this pattern(1 22 3 4444 5 666666)
for i in range(1,7):
    if i % 2 == 0:
        for j in range(1,i+1):
            print(i)
    else:
        print(i)        

