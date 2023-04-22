N = int(input())
a = 2
while a*a<= N:
    if N % a == 0:
        N //=a
        print(a)
    else :
        a+=1
if N>1:
    print(N)
