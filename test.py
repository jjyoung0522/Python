A = 9
M = 0
O = 0
for x in range (A):
    C = int(input())
    if C > M:
        M = C
        O = x+1
print (M)
print (O)
