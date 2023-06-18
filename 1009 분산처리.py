import sys

T = int(sys.stdin.readline())
test = []
for i in range(T):
    a, b = map(int, sys.stdin.readline().split())
    b = b%4
    
    if b%4 ==0 :
        b = 4
    t = a**b
    
    if t%10 == 0:
    
        test.append(10)
        
    else:
        test.append(t%10)

for i in test:
    print(i)
