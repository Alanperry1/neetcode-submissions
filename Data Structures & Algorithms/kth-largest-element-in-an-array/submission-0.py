import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        new_nums=[-i for i in nums]
        heapq.heapify(new_nums)
        while k>1:
            heapq.heappop(new_nums)
            k-=1
        return -new_nums[0]