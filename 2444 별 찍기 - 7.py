a = int(input())
for x in range(a):
    print(' '*(a-x-1)+'*'*((x+1)*2-1))
for x in range(a-1):
    print(' '*(x+1)+'*'*(a*2-1-x*2-2))
