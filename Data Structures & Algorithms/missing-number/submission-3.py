class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        hash_set={}
        nums=sorted(nums)
        for i,num in enumerate(nums):
            hash_set[i]=num
        for val in hash_set:
            if hash_set[val]!=val:
                return val


        return len(nums)

