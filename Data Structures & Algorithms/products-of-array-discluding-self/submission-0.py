import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product=[]
        for i in range(len(nums)):
            temp=nums[:i]+nums[i+1:]
            product.append(math.prod(temp))

        return product