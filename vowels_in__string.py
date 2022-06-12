x=input()
d=[]
for i in x:
    if i in 'aeiou':
        d.append(i)
    elif i in 'AEIOU':
        d.append(i)
d=sorted(set(d),key=d.index)
if d!=[]:
    print(*d)
else:
    print('-1')