x,y=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=0
for i in set(a):
    if i not in b:
        c+=1
for i in set(b):
    if i not in a:
        c+=1
print(c)