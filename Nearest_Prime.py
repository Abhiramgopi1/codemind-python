def prime(i):
    if i==1:
        return 0
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            return 0
    return 1
    
n=int(input())
for i in range(n):
    a=int(input())
    for j in range(a-1,0,-1):
        if prime(j):
            x=j
            break
    b=a    
    while True:
        if prime(b):
            y=b
            break
        b+=1
    if (a-x) <= (y-a):
        print(x)
    
    else:
        print(y)