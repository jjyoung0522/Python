inp = []
for x in range(5):
    inp.append(int(input()))
inp.sort()
print (sum(inp)//5)
print (inp[2])
