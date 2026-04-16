class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs)==0:
            return []
        
        anagram={}
        
        for str in strs:
            new=''.join(sorted(str))
            if new in anagram.keys():
                anagram[new].append(str)
            else:
                anagram[new]=[str]
        
        return list(anagram.values())