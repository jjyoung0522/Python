sum = float(0)
b= float(0)
for x in range(20):
    name,score,haks = map(str,input().split())
    score = float(score)
    if haks == 'A+':
        haks = float(4.5)
    elif haks == 'A0':
        haks = float(4.0)
    elif haks == 'B+':
        haks = float(3.5)
    elif haks == 'B0':
        haks = float(3.0)
    elif haks == 'C+':
        haks = float(2.5)
    elif haks == 'C0':
        haks = float(2.0)
    elif haks == 'D+':
        haks = float(1.5)
    elif haks == 'D0':
        haks = float(1.0)
    elif haks == 'F':
        haks = float(0.0)
    else :
        haks = float(0)
        score = float(0)
    sum += score
    b += score*haks
ans = b/sum
print (ans)
