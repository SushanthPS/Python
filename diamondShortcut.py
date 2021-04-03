n=5
m=n*2
for i in range(1,m+1):
    if i>n:
        i=i-n
        print(" "*i,"*"*((m-1)-(i*2)),sep="")
    else:
        print(" "*(n-1),"*"*((i*2)-1),sep="")