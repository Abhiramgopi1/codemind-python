l=list(map(int,input().split()))
n=sorted(l)
m=n[len(l)-1]
o=n[len(l)-2]
print((m-1)*(o-1))