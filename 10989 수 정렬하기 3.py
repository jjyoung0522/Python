import sys

N = int(sys.stdin.readline())
count = [0] * 10001

for _ in range(N):
    num = int(sys.stdin.readline())
    count[num] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i)
