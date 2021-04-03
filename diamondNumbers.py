n = 9
for i in range(0,n+1):
    print(" "*(n-i),end="")
    for j in range(0,i+1):
        print(j,end="")
    for j in range(i-1,-1,-1):
        print(j,end="")
    print()


for i in range(n,-1,-1):
    print(" "*(n-i+1),end="")
    for j in range(0,i):
        print(j,end="")
    for j in range(i-2,-1,-1):
        print(j,end="")
    print()