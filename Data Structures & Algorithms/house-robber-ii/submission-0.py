class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        def rob_II(arr):
            if len(arr)==1:
                return arr[0]
            else:
                dp=[0]*len(arr)
                dp[0]=arr[0]
                dp[1]=max(arr[0],arr[1])
                for i in range(2,len(arr)):
                    dp[i]=max(dp[i-1],arr[i]+dp[i-2])

                return dp[-1]
        case_1=rob_II(nums[:-1])
        case_2=rob_II(nums[1:])
        return max(case_1,case_2)