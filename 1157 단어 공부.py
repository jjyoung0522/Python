a = input()
b = {}
for x in a.upper():
    if x not in b:
        b[x] = 1
    else :
        b[x] += 1

M = max(b.values())
M_ = [k for k,v in b.items() if v==M]
if len(M_) == 1:
    print (M_[0])
else:
    print ('?')
