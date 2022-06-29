x=int(input())
l=list(map(int,input().split()))
s=0
for i in range(x):
    if i%2==1:
        s+=l[i]
print(s)