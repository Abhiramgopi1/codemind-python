x=input()
c=[]
d=[]
for i in x:
    if i in 'aeiou':
        c.append(i)
    elif i in 'AEIOU':
        d.append(i)
n=len(set(c))
m=len(set(d))
if n==5:
    print(True)
elif m==5:
    print(True)
else:
    print(False)