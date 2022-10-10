x=int(input())
for i in range(x):
    n=int(input())
    l=list(map(int,input().split()))
    y=((n*(n+1))//2)-sum(l)
    print(y)