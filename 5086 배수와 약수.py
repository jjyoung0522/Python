a = int(3)
while a != 0:
    f = 'factor'
    m = 'multiple'
    n = 'neither'
    a,b = map(int,input().split())
    if a == 0 and b== 0:
        break
    if a%b == 0:
        print (m)
    elif b%a == 0:
        print (f)
    else :
        print(n)
