a=int(input())
b=int(input())
for i in range(a,b+1):
    c=i
    s=len(str(i))
    a=0
    while i!=0:
        d=i%10
        i=i//10
        if d!=0 and c%d==0:
            a+=1
    if a==s:
        print(c,end=' ')