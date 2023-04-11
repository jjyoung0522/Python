a = []
n = int(9)
m = int(9)
b = int(0)
c = []
for x in range(9):
    x = list(map(int,input().split()))
    a.append(x)
for x in range(n):
    for t in range(m):
        if a[x][t]>=b :
            b = a[x][t]
            c = x+1,t+1
        else:
            pass
print (b)
print (c[0],c[1])
