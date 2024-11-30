import heapq

min_heap = []
max_heap = []
elements = [3, 1, 2, 4, 5, 6, 7, 10]

for elem in elements:
    heapq.heappush(max_heap, -elem)
    heapq.heappush(min_heap, elem)

print(min_heap)
print([-elem for elem in max_heap])
print(f"Smallest element ==> {heapq.heappop(min_heap)}")
print(f"Largest Element ==> {-heapq.heappop(max_heap)}")
