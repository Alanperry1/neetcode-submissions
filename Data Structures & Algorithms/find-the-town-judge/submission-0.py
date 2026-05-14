class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        inc=defaultdict(int)
        out=defaultdict(int)
        for incoming,outgoing in trust:
            out[incoming]+=1
            inc[outgoing]+=1
            
        for i in range(1,n+1):
            if out[i]==0 and inc[i]==n-1:
                return i
        return -1