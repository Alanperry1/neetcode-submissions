from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        maxVal=[]
        maxVal.append(nums[0])
        res=1
        for i in range(1,len(nums)):
            if maxVal[-1]<nums[i]:
                maxVal.append(nums[i])
                res+=1
            else:
                idx=bisect_left(maxVal,nums[i])
                maxVal[idx]=nums[i]
                


        return res








    