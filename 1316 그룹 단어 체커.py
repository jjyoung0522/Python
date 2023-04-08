a = int(input())
e = int(0)
for x in range(a):
    b = list(input())
    c = list(dict.fromkeys(b))
    d = len(b)
    for t in range (d):
        if b[t] not in c:
            e += 1
            break
        try:
            if b[t] != b[t+1]:
                c.remove(b[t])
        except IndexError:
                break
print(a-e)
