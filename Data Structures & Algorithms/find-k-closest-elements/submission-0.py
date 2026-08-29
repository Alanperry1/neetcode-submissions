import heapq
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        res=[]
        minHeap=[(abs(arr[i]-x),arr[i]) for i in range(len(arr))]
        heapq.heapify(minHeap)
        for i in range(k):
            a,b=heapq.heappop(minHeap)
            res.append(b)
        return sorted(res)