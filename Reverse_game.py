x = int(input())
l = list(map(int,input().split()))
for n in l:
    a=n
    s=0
    if n<0:
        n=n*-1
    while n!=0:
        i = n%10
        s = s*10+i
        n = n//10
    print(s,end=' ')