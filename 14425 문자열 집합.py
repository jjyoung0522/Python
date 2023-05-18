N , M = map(int,input().split())
s = []
check = []
result = 0
for x in range(N):
    s.append(input())
    
for x in range(M):
    check.append(input())

for x in range(M):
    if check[x] in s:
        result += 1
        
print(result)
