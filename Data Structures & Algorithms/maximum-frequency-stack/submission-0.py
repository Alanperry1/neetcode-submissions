from _heapq import heappop
import heapq
class FreqStack:

    def __init__(self):
        self.heap=[]
        self.count=defaultdict(int)
        self.index=0
        
    def push(self, val: int) -> None:
        self.count[val]+=1
        heapq.heappush(self.heap,(-self.count[val],-self.index,val))
        self.index+=1

    def pop(self) -> int:
        a,x,b=heapq.heappop(self.heap)
        self.count[b]-=1
        return b
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()