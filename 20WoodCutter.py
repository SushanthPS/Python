n,m=map(int,input().split())
arr = list(map(int,input().split()))
arr = sorted(arr)
ans = 0


def findSum(x):
    sum=0
    for i in range(n):
        if (arr[i]-x)>0:
            sum+=(arr[i]-x)
    if sum>=m:
        return True
    
low = 0
high = max(arr)

while low<=high:
    mid = low+(high-low)//2 
    if findSum(mid)==True:
        ans = mid
        low = mid+1
    else:
        high = mid-1

print(ans)
