from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.kv=defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.kv[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        vals=[r for r in self.kv[key]]
        res,l,r="",0,len(vals)-1
        while l<=r:
            mid=(l+r)//2
            if vals[mid][1]<=timestamp:
                res=vals[mid][0]
                l=mid+1
            else:
                r=mid-1
        return res

        
