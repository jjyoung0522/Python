import sys
import math
a = sys.stdin.readline

def is_prime(x):
    if x == 0 or x == 1:
        return False
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

T = int(a())
for i in range(T):
    b = int(a())
    while True:
        if is_prime(b):
            print(b)
            break
        else:
            b += 1
