x = int(input())
a,b=1,0
print(b,end=" ")
for i in range(x-1):
    c = a+b
    a,b=b,c
    print(c,end=" ")