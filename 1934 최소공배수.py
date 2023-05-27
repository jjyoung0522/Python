def gcd(a, b):
    while(b != 0):
        r = a % b
        a = b
        b = r
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

T = int(input())
ans = list()

for x in range(T):
    a, b = map(int, input().split())
    ans.append(lcm(a, b))

for x in range(T):
    print(ans[x])
