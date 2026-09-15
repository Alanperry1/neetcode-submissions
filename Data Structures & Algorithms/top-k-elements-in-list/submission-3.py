from _heapq import heapify
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res=[]
        freq=Counter(nums)
        minHeap=[(-b,a) for a,b in freq.items()]
        heapq.heapify(minHeap)
        for i in range(k):
            x,y=heapq.heappop(minHeap)
            res.append(y)
        return res