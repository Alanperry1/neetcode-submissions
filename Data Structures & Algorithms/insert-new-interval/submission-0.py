class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        l,r=0,len(intervals)-1
        target=newInterval[0]
        res=[]
        while l<=r:
            mid=(l+r)//2
            if intervals[mid][0]<target:
                l=mid+1
            else:
                r=mid-1


        intervals.insert(l,newInterval)    
        for i in intervals:
            if not res or res[-1][1]<i[0]:
                res.append(i)
            else:
                res[-1][1]=max(res[-1][1],i[1])

        return res