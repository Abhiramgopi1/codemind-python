x,y=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[]
for i in sorted(set(a),key=a.index):
    if i in b:
        c.append(i)
print(*c)