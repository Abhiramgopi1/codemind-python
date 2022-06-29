x = int(input())
l = list(map(int,input().split()))
for i in range(x):
    if l[i]%2==1:
        m = i
print(m)