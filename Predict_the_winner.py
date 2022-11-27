n=int(input())
l=list(map(int,input().split()))
x=0
y=0
for i in range(len(l)):
    if(i%2==0):
        x+=l[i]
    if(i%2!=0):
        y+=l[i]
if(abs(x-y)%4==0):
    print("X")
else:
    print("Y")