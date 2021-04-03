n=5
k=1
for i in range(1,n+1):
    print(" "*(n-i),end="")
    print("*"*k,end="")
    print()
    k+=2

k=k-4
for i in range(1,n+1):
    print(" "*i,end="")
    print("*"*k,end="")
    print()
    k-=2