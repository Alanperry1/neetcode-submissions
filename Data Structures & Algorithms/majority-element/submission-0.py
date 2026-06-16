class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num=Counter(nums)
        for a,b in num.items():
            if b>len(nums)//2:
                return a
