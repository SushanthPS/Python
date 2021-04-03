n=int(input())
arr=list(map(int,input().split()))[:n]
b=set(arr)
ans1=-1
ans2=-1

for i in b:
    count=0
    for j in range(n):
        if i==arr[j]:
            count+=1

    if count>ans1:
        ans1=count
        ans2=i

print("Mode: ",ans2)
print("Count: ",ans1)