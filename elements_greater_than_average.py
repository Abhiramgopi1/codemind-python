x = int(input())
l=list(map(int,input().split()))
s = float(sum(l)//len(l))
c=0
for i in l:
    if s<=i:
        c+=1
print(c)