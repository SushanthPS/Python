
def isprime(n):
    if n==1:
        return False
    elif n==2 or n==3:
        return True
    elif n%2==0:
        return False
    else:
        for i in range(3,n//2,2):
            if n%i==0:
                return False
        return True
    

print(isprime(13))