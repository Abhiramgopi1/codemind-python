def prime(i):
    if i==1:
        return 0
    for j in range(2,i//2):
        if i%j==0:
            return 0
    return 1

n=int(input())
if prime(n):
    print('prime')
else:
    print('not a prime')