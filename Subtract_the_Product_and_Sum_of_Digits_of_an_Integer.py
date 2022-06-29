x = input()
s=0
m=1
for i in x:
    s+=int(i)
    m*=int(i)
print(m-s)