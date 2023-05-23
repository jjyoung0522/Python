from collections import Counter

N = int(input())
have = set(map(int, input().split()))

M = int(input())
find = list(map(int, input().split()))
counter = Counter(find)

ans = [counter[x] if x in have else 0 for x in find]

for count in ans:
    print(count, end=' ')
