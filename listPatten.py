test = int(input())
for i in range(test):

    n=int(input())
    arr=list(map(int,input().split()))[:n]
    ans="NO"

    for i in range(0,n-3):
        if arr[i]==0 and arr[i+1]==1 and arr[i+2]==2 and arr[i+3]==3:
            ans="YES"
            break
        
    print(ans)