N = int(input())
ansx = [x for x in range(N)]
ansy = [x for x in range(N)]
for x in range(N):
    ansx[x],ansy[x] = map(int,input().split())
print ((max(ansx) - min(ansx)) * (max(ansy) - min(ansy)))
