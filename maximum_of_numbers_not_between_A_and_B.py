x=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
n=[]
m=1
for i in range(x):
    if l[i]>=a and l[i]<=b:
        pass
    else:
        n.append(l[i])
        m=0
if m==1:
    print('-1')
else:
    print(max(n))