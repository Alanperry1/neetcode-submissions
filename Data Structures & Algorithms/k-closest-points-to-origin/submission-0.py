import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_Heap=[]
        for a,b in points:
            distance=(a**2)+(b**2)
            min_Heap.append([distance,a,b])

        heapq.heapify(min_Heap)
        result=[]
        while k>0:
            distance,a,b=heapq.heappop(min_Heap)
            result.append([a,b])
            k-=1
        return result