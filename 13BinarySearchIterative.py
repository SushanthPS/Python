n , k = map(int,input().split())
a = list(map(int,input().split()))[:n]
a = sorted(a)
low=0
high=n-1
ans=-1
while low<=high:
    mid=low+(high-low)//2
    if k==a[mid]:
        ans=1
        break
    elif k>a[mid]:
        low=mid+1
    else:
        high=mid-1

print(ans)