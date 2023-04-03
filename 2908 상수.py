a,b = map(str,input().split())
a = int(a[::-1])
b = int(b[::-1])
if a < b:
    c = b
else :
    c = a
print (c)
