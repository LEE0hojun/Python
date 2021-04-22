import random

Num=[0,0,0,0,0,0]
now=0
count=0

for x in range(6):

    while True:
        count=0        
        now=random.randrange(1,46)        
        for y in range(6):
            if Num[y]==now:
                count=count+1
              
        if count==0:
            break

    Num[x]=now
    
Num.sort()

print(Num)
