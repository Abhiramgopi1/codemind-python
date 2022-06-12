x=input()
y=input()
for i in range(len(x)):
    if x[i]==y:
        print(True)
        print(i)
        break
else:
    print(False)