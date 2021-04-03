stack = []
n = int(input())
for i in range(n):
    lst = []   
    lst = [int(item) for item in input().split()] 
    if lst[0] == 1:
        stack.append(lst[1])
    elif lst[0] == 2:
        if len(stack)!=0:
            stack.pop()
    elif lst[0] == 3:
        if len(stack) == 0:
            print("Empty!")
        else:
            print(stack[-1])

            
    
    
