
n, target= map(int,input().split())
lst = list(map(int,input().split()))[0:n]
pairs = 0

for i in range(len(lst)-1):
    for j in range(i+1,len(lst)):
        if lst[i]+lst[j]==target:
            pairs+=1

print(pairs)
