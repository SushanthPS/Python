n , q = map(int,input().split())
arr = list(map(int,input().split()))[:n]
arr = sorted(arr)


while q>0:

    query = int(input())
    low = 0
    high = n-1
    while low<=high:
        ans = "NO"
        mid = low + (high-low)//2
        if query == arr[mid]:
            ans = "YES"
            break
        elif query>arr[mid]:
            low = mid+1
        else:
            high = mid-1
    print(ans)
    q-=1
    
    


