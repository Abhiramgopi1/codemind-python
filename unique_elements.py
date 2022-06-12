x=int(input())
l=list(map(int,input().split()))
j=sorted(set(l),key=l.index)
for i in j:
    print(i,end=" ")