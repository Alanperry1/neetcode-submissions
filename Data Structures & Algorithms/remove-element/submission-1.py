class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # while val in nums:
        #         nums.remove(val)

        # return len(nums)
        k=0
        for i in nums:
            if i!=val:
                nums[k]=i
                k+=1
        return k