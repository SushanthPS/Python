n = int(input())
a = list(map(int,input().split()))[:n]
a = sorted(a)
q = int(input())


while q!=0:
    option,x=map(int,input().split())
    low = 0
    high = n-1
    ans=-1
    while low<=high:
        mid=low+(high-low)//2
        if option==0:
            if a[mid]>=x:
                ans=mid
                high=mid-1
            else:
                low=mid+1


        elif option==1:
            if a[mid]>x:
                high=mid-1
                ans=mid
            else:
                low=mid+1
    
    if ans==-1:
        print("0")
    else:
        print(n-ans)
    
    q-=1



    

