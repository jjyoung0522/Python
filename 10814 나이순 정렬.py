N = int(input())
information = []

for _ in range(N):
    age, name = input().split()
    information.append((int(age), name))

sorted_information = sorted(information, key=lambda x: x[0])

for person in sorted_information:
    print(person[0], person[1])
