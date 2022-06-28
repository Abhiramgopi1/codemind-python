n=int(input())
i=n*n
s=0
while i:
    d=i%10
    i=i//10
    s+=d
if s==n:
    print('Neon Number')
else:
    print('Not Neon Number')