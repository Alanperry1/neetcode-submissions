import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        maxProfit=[]
        minHeap=[(capital[i],profits[i]) for i in range(len(capital))]
        heapq.heapify(minHeap)
        
        for x in range(k):
            while minHeap and minHeap[0][0]<=w:
                c,p=heapq.heappop(minHeap)
                heapq.heappush(maxProfit,-p)


            if not maxProfit:
                break

            w+=-heapq.heappop(maxProfit)

        return w