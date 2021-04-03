def isPalindrome(s):
    i=0
    j=len(s)-1
    val=True
    while i<j:
        if s[i]!=s[j]:
            val=False
            break
        i=i+1
        j=j-1
    return val

s=input()
ans=0
for i in range(len(s)):
    for j in range(i,len(s)):
        substr=s[i:j+1]
        if isPalindrome(substr):
            ans=max(ans,len(substr))
print(ans)


