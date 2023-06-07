import sys
import heapq

def heap_sort(numbers):
    heap = []
    for number in numbers:
        heapq.heappush(heap, number)
    
    sorted_numbers = []
    while heap:
        sorted_numbers.append(heapq.heappop(heap))
    
    return sorted_numbers


n = int(sys.stdin.readline())

average_people = int(n * 0.15 + 0.5)
point = []
average = 0

for x in range(n):
    point.append(int(sys.stdin.readline()))
point_sort = heap_sort(point)

for x in range(average_people, n - average_people):
    average += point_sort[x]
    
if n != 0:
    point = int(average / (n - average_people * 2) + 0.5)
else:
    point = 0
    
print(point)
