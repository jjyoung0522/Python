N , M = map(int,input().split())
A = [x for x in range(1,N+1)]

for x in range(M):
    b,c = map(int,input().split())
    d = A[b-1]
    A[b-1] = A[c-1]
    A[c-1] = d
    
for y in range(N):
    print(A[y],end = ' ')
