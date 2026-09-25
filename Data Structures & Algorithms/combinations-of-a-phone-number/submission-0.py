class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res=[]
        dig_char={
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"qprs",
            "8":"tuv",
            "9":"wxyz",
        }

        def backtrack(i,curr):
            if len(curr)==len(digits):
                res.append(curr)
                return
            for k in dig_char[digits[i]]:
                backtrack(i+1,curr+k)


        if digits:

            backtrack(0,'')

        return res