x=int(input())
l=list(map(int,input().split()))
n = float(sum(l)/len(l))
c=0
for i in l:
    if n>=i:
        c+=1
print(c)