n,m = map(int,input().split())
a1,a2 = [],[]
for x in range (n):
    x = list(map(int,input().split()))
    a1.append(x)
for x in range (n):
    x = list(map(int,input().split()))
    a2.append(x)    
for x in range (n):
    for t in range(m):
        print(a1[x][t]+a2[x][t],end = ' ')
    print()
