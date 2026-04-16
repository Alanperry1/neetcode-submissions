class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hash_set={}
        for i in nums:
            if i in hash_set:
                hash_set[i]+=1
            else:
                hash_set[i]=1
        for key, val in hash_set.items():
            if val > 1:
                return key