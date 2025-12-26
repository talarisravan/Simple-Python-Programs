n=15
m=20
if n>m:
    x=m
else:
    x=n
def gcd(n,m,x):
    for i in range(x,0,-1):
        if n%i==0 and m%i==0:
            return i
print(gcd(n,m,x))