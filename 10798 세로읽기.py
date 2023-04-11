a= []
b = ()
for x in range (5):
    x = list(input())
    a.append(x)
    if len(b)<len(x):
        b=x
b=len(b)
for x in range (b):
    for t in range(5):
        try:
            print(a[t][x],end='')
        except:
            pass
