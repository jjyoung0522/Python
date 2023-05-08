N = int(input())
box5 = N // 5

while box5 >= 0:
    if (N - 5 * box5) % 3 == 0:
        box3 = (N - 5 * box5) // 3
        print(box5 + box3)
        break
    box5 -= 1

if box5 < 0:
    print(-1)
