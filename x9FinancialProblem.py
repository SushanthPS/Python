test = int(input())
for i in range(test):

    n = int(input())
    lst = list(map(int,input().split()))[:n]
    stock = [1] 

    for i in range(1,n):
        sum = 1
        j=i-1
        while lst[i]>=lst[j] and j>=0:
            sum+=1
            j=j-1
        stock.append(sum)

    print(*stock)



         

""" 0       1       2       3       4       5  =  Index
    100     60      70      65      80      85 =  lst
    1       1       2       1       4       5  =  stock """