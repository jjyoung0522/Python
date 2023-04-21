def prime_number(n):
    if n < 2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

M = int(input())
N = int(input())
answer = []
for i in range(M,N+1):
    if prime_number(i):
        answer.append(i)

if not answer:
    print('-1')
else:
    print (sum(answer))
    print (min(answer))
