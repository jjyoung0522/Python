n,m = map(int,input().split())
count = m-n+1
divisible = [False] * (count)

for i in range(2, int(m**0.5+1)):
    chae = i ** 2
    for j in range((((n-1)//chae)+1)*chae, m+1, chae):
        if not divisible[j-n]:
            divisible[j-n] = True
            count -= 1

print(count)
