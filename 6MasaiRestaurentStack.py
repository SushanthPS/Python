cost = []
q = int(input())
for i in range(q):
    lst = list(map(int,input().split()))
    if lst[0]==1:
        if len(cost)==0:
            print("No Food")
        else:
            print(cost.pop())
            
    elif lst[0]==2:
        cost.append(lst[1])

