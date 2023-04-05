N,M = map(int,input().split())
a = [x+1 for x in range(N)]
b = [x+1 for x in range(N)]
for x in range(M):
    i,j,k = map(int,input().split())
    for t in range (j-k+1):
        a[i-1+t] = b[k-1+t]
    for t in range (k-i):
        a[j-k+i+t] = b[i-1+t]
    b = a.copy()
for x in range(N):
    print (a[x],end=' ')
