n = int(input())
a = int(1)
a_p = int(6)
ans = int(1)
while n != a:
    ans += 1
    a += a_p
    if a <= n:
        a_p += 6
    else :
        break
print (ans)
