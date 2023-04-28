a = list(map(int,input().split()))
a.sort()
if a[2] >= a[0]+a[1]:
    a[2] = a[0]+a[1] -1
    ans = sum(a)
else :
    ans = sum(a)
print (ans)
