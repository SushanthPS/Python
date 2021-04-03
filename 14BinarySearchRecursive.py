def binarySearch(low,high,a,k):
    
    if low<=high:
        mid = (low+high)//2
        if a[mid]==k:
            print("1")
        elif a[mid]>k:
            return binarySearch(low,mid-1,a,k)
        elif a[mid]<k:
            return binarySearch(mid+1,high,a,k)
    else:
        print("-1")



n , k = map(int,input().split())
a = list(map(int,input().split()))[:n]
a = sorted(a)

binarySearch(0,n-1,a,k)
