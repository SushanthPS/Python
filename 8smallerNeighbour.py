n = int(input())
lst = list(map(int,input().split()))[:n]
output = [-1]

for i in range(1,n):
    if lst[i-1]<lst[i]:
        output.append(lst[i-1])
    else:
        for j in range(i-1,-1,-1):
            if output[j]<lst[i]:
                output.append(output[j])
                break

print(*output)