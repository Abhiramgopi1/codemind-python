def prime(i):
    if i==1:
        return 0
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            return 0
    return 1
n=int(input())
l=list(map(int,input().split()))
c=0
k=int(input())
for i in l:
    if i>=k:
        if prime(i):
            c+=1
print(c)