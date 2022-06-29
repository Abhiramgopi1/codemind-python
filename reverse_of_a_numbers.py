x=int(input())
s=0
while x:
    d=x%10
    s=s*10+d
    x=x//10
print(s)