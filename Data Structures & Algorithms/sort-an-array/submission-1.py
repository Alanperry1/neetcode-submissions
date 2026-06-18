class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
     
        count=defaultdict(int)
        for num in nums:
            count[num]+=1
        index=0
        for i in range(min(nums),max(nums)+1):
            while count[i]:
                count[i]-=1
                nums[index]=i
                index+=1
        return nums
            
        