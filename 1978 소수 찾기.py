a = int(input())
c = input()
c = list(map(int,c.split()))
d = int(0)
for x in range(a):
    b = []
    for i in range(c[x]):
        if c[x] % (i+1) == 0:
            b.append(i+1)
    if len(b) == 2:
        d += 1
print(d)
