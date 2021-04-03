count = 0
n , k = map(int,input().split())
a = list(map(int,input().split()))[:n]
low = 0
high = n-1

while low<=high:
    mid = low+(high-low)//2
    if a[mid]==k:
        count=count+1
        a.pop(mid)
        high=len(a)-1
        if len(a)==0:
            break
        
    elif k<a[mid]:
        high=mid-1
    elif k>a[mid]:
        low=mid+1
print(count)
    