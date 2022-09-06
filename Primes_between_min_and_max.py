def prime(n):
    if n==1:
        return 0
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    return 1
x=int(input())
l=list(map(int,input().split()))
c=0
n=l.index(max(l))
m=l.index(min(l))
if m<n:
    for i in range(m,n+1):
        if prime(l[i]):
            c+=1
else:
    for i in range(n,m+1):
        if prime(l[i]):
            c+=1
print(c)
        