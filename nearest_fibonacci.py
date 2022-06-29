def fib(i):
    a=0
    b=1
    c=a+b
    while c<i:
        c=a+b
        a=b
        b=c
    if c==i:
        return i
        
x=int(input())
k=x
for i in range(x,0,-1):
    if fib(i):
        a=i
        break
while k!=0:
    if fib(k):
        b=k
        break
    k+=1
if (x-a)<(b-x):
    print(a)
elif (x-a)==(b-x):
    print(a,b)
else:
    print(b)