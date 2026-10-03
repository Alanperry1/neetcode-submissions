class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        new=[i for i in range(1,len(nums)+1)]
        res=[]
        for num in new:
            if num not in nums:
                res.append(num)
        return res