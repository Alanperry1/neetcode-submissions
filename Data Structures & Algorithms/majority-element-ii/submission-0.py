class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        floor=n//3
        result=[]
        from collections import Counter
        hash_set=Counter(nums)
        for val in hash_set:
            if hash_set[val]>floor:
                result.append(val)
        return result
