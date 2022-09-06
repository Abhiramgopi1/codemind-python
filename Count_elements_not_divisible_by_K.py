x,y=map(int,input().split())
a=list(map(int,input().split()))
d=0
for i in a:
    if i%y!=0:
        d+=1
print(d)
