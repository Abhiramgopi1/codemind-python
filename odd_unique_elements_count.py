x=int(input())
l=set(map(int,input().split()))
c=0
for i in l:
    if i%2==1:
        c+=1
print(c)