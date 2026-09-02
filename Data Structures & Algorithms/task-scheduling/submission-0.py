class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c=Counter(tasks)
        maxCurr=max(c.values())
        num_max=sum(1 for x in c.values() if x==maxCurr)
        intervals= (maxCurr-1)*(n+1)+num_max


        return max(len(tasks), intervals)