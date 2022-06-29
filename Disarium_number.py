x = input()
s=0
for i in range(len(x)):
    s+=(int(x[i])**(i+1))
if s==int(x):
    print(True)
else:
    print(False)