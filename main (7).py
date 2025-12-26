def check_prime(n):
    if n<=1:
        return"not a prime number"
    for i in range(2,n):
        if n%i==0:
            return"not a prime number"
        return"prime number"
print(check_prime(-19))    