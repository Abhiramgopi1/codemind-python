n=int(input())
q=n*n
c=len(str(n))
d=q%(10**c)
if d==n:
    print('Automorphic Number')
else:
    print('Not an Automorphic Number')