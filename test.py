def binarySearch(low,high,a,k,count):
    
    if low<=high:
        mid = (low+high)//2
        if a[mid]==k:
            count=count+1
            a.pop(mid)
            high=len(a)-1
            if(len(a)==0):
                break
                        
        elif a[mid]>k:
            return binarySearch(low,mid-1,a,k,count)
        elif a[mid]<k:
            return binarySearch(mid+1,high,a,k,count )
    print(count)
        
        
    
count = 0
n , k = map(int,input().split())
a = list(map(int,input().split()))[:n]


binarySearch(0,n-1,a,k,count)

