x=input()
y=['a','e','i','o','u']
c=[]
d=0
for i in x:
    if i=='a' or i=='e' or i=='o' or i=='i' or i=='u':
        c.append(i)
if len(set(c))==len(y):
    print('0')
else:
    for j in y:
        for k in list(set(c)):
            if j==k:
                d+=1
        if d==0:
            print(j,end=" ")
        d=0