x=int(input())
l=list(map(int,input().split()))
c=0
for i in set(l):
    if i%2==0:
        c+=i
print(c)