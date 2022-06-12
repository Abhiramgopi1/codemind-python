x=input()
c=0
for i in x:
    if i>='a' and i<='z':
        pass
    elif i>='A' and i<='Z':
        pass
    elif i==' ':
        pass
    else:
        c+=1
print(c)