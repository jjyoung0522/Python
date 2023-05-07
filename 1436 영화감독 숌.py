N = int(input())
test = 0
name = 666
while True:
    if '666' in str(name):
        test += 1
    if test == N:
        print(name)
        break
    name += 1
