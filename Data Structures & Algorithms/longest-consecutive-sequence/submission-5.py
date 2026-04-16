class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        new=sorted(set(nums))
        count=1
        longest=1
        i=0
        while i<len(new)-1:
            if abs(new[i+1]-new[i])==1:
                count+=1
            else:
                longest = max(longest, count)
                count = 1
            i+=1
        
        return max(longest,count)