def isprime(n):
    if n==1:
        return False
    else:
        for i in range(2,n//2+1):
            if n%i==0:
                return False

    return True

n = int(input())
lst = list(map(int,input().split()))[:n]
sum = 0

for i in range(len(lst)-1):
    for j in range(i+1,len(lst)):
        if isprime(j-i):
            sum=sum+abs(lst[j]-lst[i])

print(sum)