import heapq

# Creating a heap
heap = []

# Or convert a list to a heap in-place
my_list = [5, 7, 9, 1, 3]
heapq.heapify(my_list)
print("Heapified list:", my_list)

# Adding elements to the heap
heapq.heappush(heap, 5)
heapq.heappush(heap, 7)
heapq.heappush(heap, 9)
heapq.heappush(heap, 1)
heapq.heappush(heap, 3)
print("Heap after adding elements:", heap)

smallest = heapq.heappop(heap)
print("Smallest element popped from heap:", smallest)
print("Heap after popping smallest element:", heap)
print("Peek smallest element in the heap:", heap[0])

smallest_three = heapq.nsmallest(3, heap)
print("Three smallest elements in the heap:", smallest_three)
largest_three = heapq.nlargest(3, heap)
print("Three largest elements in the heap:", largest_three)


