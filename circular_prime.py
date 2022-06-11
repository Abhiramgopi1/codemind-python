def prime(i):
    if i==1:
        return 0
    for j in range(2,i//2):
        if i%j==0:
            return 0
    return 1

x=int(input())
r=0
a=x
while x!=0:
    d=x%10
    r=r*10+d
    x//=10
if prime(r) and prime(a):
    print('circular prime')
elif (prime(a)):
        print('prime but not a circular prime')
else:
    print('not prime')