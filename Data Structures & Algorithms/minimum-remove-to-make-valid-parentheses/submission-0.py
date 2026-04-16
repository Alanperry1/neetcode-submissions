class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack=[]
        result=[]
        invalid_paren=set()
        for i,char in enumerate(s):
            if char=="(":
                stack.append(i)
            elif char==")":
                if stack:
                    stack.pop()
                else:
                    invalid_paren.add(i)
        invalid_paren.update(stack)
        for i,char in enumerate(s):
            if i not in invalid_paren:
                result.append(s[i])
        return "".join(result)