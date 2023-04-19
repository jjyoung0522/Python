t = int(input())
t_p = int(1)
ans_n = int(1)
while ans_n <= t:
    ans_n += t_p
    t_p += 1
ans_n -= t_p-1
front = t-ans_n+1 
back = t_p-front
if (t_p-1)%2 == 0 :
    print (f'{front}/{back}')
else :
    print(f'{back}/{front}')
