N,K = map(int,input().split())
K_A = int(0)
for x in range(1,N+1):
    if N%x == 0:
        K_A += 1
    if K_A == K:
        K_A = x
        break
if K_A < K:
    K_A = 0
print(K_A)
