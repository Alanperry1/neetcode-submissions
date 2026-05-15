import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k=k
        self.heap=[]
        for n in nums:
            self.add(n)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap,val)
        if len(self.heap)>self.k:
            heapq.heappop(self.heap)
        return self.heap[0]

# class KthLargest:

#     def __init__(self, k: int, nums: List[int]):
#         self.minHeap, self.k = nums, k
#         heapq.heapify(self.minHeap)
#         while len(self.minHeap) > k:
#             heapq.heappop(self.minHeap)

#     def add(self, val: int) -> int:
#         heapq.heappush(self.minHeap, val)
#         if len(self.minHeap) > self.k:
#             heapq.heappop(self.minHeap)
#         return self.minHeap[0]