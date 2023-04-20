while True:
    a = int(input())
    b = []
    if a == -1:
        break
    for x in range(1,a):
        if a % x == 0:
            b.append(x)
    d = sum(b)
    if a == d :
        e = f"{a} = "
        for x in range(len(b)):
            e += str(b[x])
            if x < len(b) - 1 :
                e+= " + "
        print(e)
    else :
        print (f'{a} is NOT perfect.')
