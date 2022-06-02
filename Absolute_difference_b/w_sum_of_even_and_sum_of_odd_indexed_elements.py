a=int(input())
l=list(map(int,input().split()))
m,n=0,0
for i in range(len(l)):
    if i%2==0:
        m+=l[i]
    else:
        n+=l[i]
print(abs(m-n))