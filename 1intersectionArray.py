n=int(input())
lst1=list(map(int,input().split()))[:n]
lst2=list(map(int,input().split()))[:n]

for i in lst1:
    for j in lst2:
        if i==j:
            print(i)
            break
  