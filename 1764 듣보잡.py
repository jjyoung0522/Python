N,M = map(int,input().split())
detdo = set()
bodo = set()
for x in range(N):
    detdo.add(input())
for x in range(M):
    bodo.add(input())
ans = sorted(detdo&bodo)
print(len(ans))    
for x in ans:
    print(x)
