q = int(input())
stack = []
queue = []
for i in range(q):
    lst=list(map(int,input().split()))
    if lst[0] == 1:
        queue.append(lst[1])
    elif lst[0] == 2:
        stack.append(lst[1])
    elif lst[0] == 3:
        if len(queue)==0:
            print("-1")
        else: 
            print(queue[0])
    elif lst[0] == 4:
        if len(stack)==0:
            print("-1")
        else:
            print(stack[-1])
    elif lst[0] == 5:
        stack.append(queue.pop(0))

