N = int(input())
ans = []
for _ in range(N):
    x, y = map(int, input().split())
    ans.append((x, y))

ans.sort(key=lambda p: (p[1], p[0]))

for x, y in ans:
    print(x, y)
