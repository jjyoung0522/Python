N = int(input())
num = []
for x in range(N):
    num.append(int(input()))
num.sort()
for x in range(N):
    print(num[x])
