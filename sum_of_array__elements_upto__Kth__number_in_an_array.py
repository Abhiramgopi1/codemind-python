x = int(input())
l = list(map(int,input().split()))
y = int(input())
c=0
for i in l:
    c+=i
    if i==y:
        break
print(c)