string = input()
n=len(string)
sub=""
count=0
for i in range(n):
    for j in range(i+1,n+1):
        sub=string[i:j] 
        print(sub)        
        if sub[0]==sub[-1]:
            count+=1

print(count)
        



