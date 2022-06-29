x=int(input())
y=list(map(int,input().split()))
c=0
for i in set(y):
    if i%2==0:
        c+=1
print(c)