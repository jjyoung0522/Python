import sys

N = int(sys.stdin.readline())
num = []
for x in range(N):
    num.append(int(sys.stdin.readline()))
num.sort()
for x in range(N):
    print(num[x])
