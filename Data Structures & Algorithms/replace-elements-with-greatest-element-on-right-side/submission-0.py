class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxright=-1
        ans=[0]*len(arr)
        for r in range(len(arr)-1,-1,-1):
            ans[r]=maxright
    
            maxright=max(maxright,arr[r])
        return ans 
