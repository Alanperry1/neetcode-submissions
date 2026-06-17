class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum=defaultdict(int)
        total,curr=0,0
        for num in nums:
            prefixSum[curr]+=1
            curr+=num
            total+=prefixSum[curr-k]

        return total