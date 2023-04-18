T = int(input())
for x in range (T):
    a = int(input())
    Qu = a//25
    a = a%25
    Di = a//10
    a = a%10
    Ni = a//5
    a = a%5
    Pe = a
    print (Qu,Di,Ni,Pe)
