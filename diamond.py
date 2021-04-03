n=5
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(i):
        print("* ",end="")
    print()

k=1
for i in range(n-1,-1,-1):
    print(" "*k,end="")
    print("* "*i,end="")
    print()
    k+=1
