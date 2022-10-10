x=int(input())
l=[]
for i in range(x):
    l.append(int(input()))
y=int(input())
c=0
for i in l:
    if i<=y:
        c+=1
    else:
        c+=2
print(c)
         