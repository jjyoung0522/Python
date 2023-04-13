a = int(input())
origin = []
for t in range(100):
    origin.append([])
    for x in range(100):
        origin[t].append(0)
for p in range(a):
    x,y = map(int,input().split())
    for i in range(x-1,x+9):
        for q in range(y-1,y+9):
            origin[i][q] = 1
ans = int(0)
for t in range(100):
    for k in range(100):
        ans += origin[t][k]
print (ans)
