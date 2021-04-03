n , k = map(int,input().split())
a = list(map(int,input().split()))[:n]

low=0
high=n-1
index=n

while low<=high:
    mid=low+(high-low)//2
    if a[mid]>k and mid<index:
        index=mid
        high = mid-1
    else:
        low = mid+1

print(index)
