import heapq
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x:x[1])
        currPass=0
        minHeap=[]

        for numP,start,finish in trips:
            while minHeap and minHeap[0][0]<=start:
                currPass-=heapq.heappop(minHeap)[1]
            currPass+=numP
            if currPass>capacity:
                return False           
            heapq.heappush(minHeap,[finish,numP])
        return True