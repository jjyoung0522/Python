import sys
N = int(sys.stdin.readline())
test = set(map(int,input().split()))
M = int(sys.stdin.readline())
comparison = list(map(int,input().split()))

for x in comparison:
    if x in test:
        print ('1')
    else:
        print('0')
