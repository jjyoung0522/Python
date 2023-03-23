N,M = map(int,input().split())
A = [0 for _ in range(N)]
for _ in range(M):
    b,c,d = map(int,input().split())
    for x in range(b,c+1):
        A[x-1] = d
for y in range(N):
    print (A[y],end=' ')
