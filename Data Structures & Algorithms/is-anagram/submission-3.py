class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen_1={}
        seen_2={}
        if len(s)!= len(t):
            return False
        
        for c in s:
            if c in seen_1:
                seen_1[c]+=1
            else:
                seen_1[c]=1


        for char in t:
            if char in seen_2:
                seen_2[char]+=1
            else:
                seen_2[char]=1

        if seen_1==seen_2:
            return True
        else:
            return False