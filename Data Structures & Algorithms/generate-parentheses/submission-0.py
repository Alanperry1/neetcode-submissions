class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #Total number of pairs in each element= n*2
        #Total number of closed bracket=Total number of open bracket
        #if close<open append close

        stack=[]
        res=[]
        def backtrack(openB,closeB):
            if openB==closeB==n:
                res.append("".join(stack))
            if closeB<openB:
                stack.append(")")
                backtrack(openB,closeB+1)
                stack.pop()
            if openB<n:
                stack.append("(")
                backtrack(openB+1,closeB)
                stack.pop()
        backtrack(0,0)
        return res