x=int(input())
l=list(map(int,input().split()))
s,c=0,0
for i in l:
    if i%2==0:
        s+=i
    else:
        c+=i
print(abs(s-c))