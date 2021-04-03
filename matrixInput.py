R = int(input("Enter the number of rows:")) 
C = int(input("Enter the number of columns:")) 

matrix=[]
#1st input method
for i in range(R):
    a=list(map(int,input().split()))[:C]
    matrix.append(a)

#2nd input method
""" for i in range(R):
    a=[]
    for j in range(C):
        a.append(int(input()))
    matrix.append(a) """

#3rd input method
""" matrix=[[int(input()) for i in range(R)]for j in range(C)]
 """

#1st output method
print()
print("FIRST OUTPUT METHOD")
print(matrix)

#2nd output method
print()
print("SECOND OUTPUT METHOD")
for i in range(R):
    print(matrix[i])

#3rd output method
print()
print("THIRD OUTPUT METHOD")
for i in range(R):
    for j in range(C):
        print(matrix[i][j],end=" ")
    print()