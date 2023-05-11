import sys

N = list(sys.stdin.readline().strip())
N.sort(reverse=True)
ans = ''.join(N)  
print(ans)
