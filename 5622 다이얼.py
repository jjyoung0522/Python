a = list(input())
b = int(0)
for x in range(len(a)):
    if a[x] == 'A' or a[x]=='B' or a[x]=='C':
        a[x] = int(3)
    elif a[x] == 'D' or a[x]=='E' or a[x]=='F':
        a[x] = int(4)
    elif a[x] == 'G' or a[x]=='H' or a[x]=='I':
        a[x] = int(5)
    elif a[x] == 'J' or a[x]=='K' or a[x]=='L':
        a[x] = int(6)
    elif a[x] == 'M' or a[x]=='N' or a[x]=='O':
        a[x] = int(7)
    elif a[x] == 'P' or a[x]=='Q' or a[x]=='R' or a[x]=='S':
        a[x] = int(8)
    elif a[x] == 'T' or a[x]=='U' or a[x]=='V':
        a[x] = int(9)
    elif a[x] == 'W' or a[x]=='X' or a[x]=='Y' or a[x]=='Z':
        a[x] = int(10)
    b += a[x]
print(b)
