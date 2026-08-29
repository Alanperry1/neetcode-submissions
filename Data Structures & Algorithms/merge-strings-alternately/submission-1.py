class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1,l2=len(word1),len(word2)
        k=0
        res=""
        while k<min(l1,l2) and word1 and word2:
           res+=word1[k]+word2[k]
           k+=1
        if l1==l2:
            return res
        else:
            longer = word1 if l1 > l2 else word2
            res += longer[k:]
            return res