x = int(input())
l = list(map(int,input().split()))
s=0
d=0
for i in range((x//2)):
    s+=l[i]
print(s)
for j in range(x//2,x):
    d+=l[j]
print(d)