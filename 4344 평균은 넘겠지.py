a = int(input())
for x in range(a):
    d = int(0)
    b = input().split()
    c = int(b[0])
    e = int(0)
    for t in range(c):
        d += float(b[t+1])
        avg = d/c
    for t in range(c):
        if float(b[t+1]) > avg:
            e += 1
        else :
            pass
    ans = 100/c*e
    print ("{0:.3f}%".format(ans))
