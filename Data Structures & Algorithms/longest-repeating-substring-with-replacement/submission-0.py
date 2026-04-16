class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #hash-set of frequency of elements
        #set two pointer
        result=0
        hash_set={}
        l=0
        for r in range(len(s)):
            hash_set[s[r]]=hash_set.get(s[r],0)+1
            #setting the window size r-l+1
            while (r-l+1)-max(hash_set.values())>k:
                hash_set[s[l]]-=1
                l+=1
            result=max(result,r-l+1)
        return result

    