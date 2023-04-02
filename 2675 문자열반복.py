e = str()
a = int(input())
for x in range(a):
    e = str()
    b,c = map(str,input().split())
    b = int(b)
    d = len(c)
    for k in range(d):
        e += (c[k]*b)
    print (e)
