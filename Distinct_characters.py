x = input()
c=0
for i in sorted(set(x)):
    if i>='a' and i<='z':
        print(i,end='')