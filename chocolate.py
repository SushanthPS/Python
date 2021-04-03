test = int(input())
for i in range(test):

    points = int(input())
    n = points

    if points<10:
        ans = points

    else:
        summ=points
        while n!=0:
            n = n//10
            summ += n
        ans = points + (summ//10)

    print(ans)
    print()
        


         

        
