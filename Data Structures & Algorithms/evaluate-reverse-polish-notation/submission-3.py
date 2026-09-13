class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for char in tokens:
            if char not in "+-*/":
                stack.append(int(char))
            else:
                a=int(stack.pop())
                b=int(stack.pop())


                if char=="+":
                    res=a+b
                    stack.append(res)
                elif char=="-":
                    res=b-a
                    stack.append(res)
                elif char=="*":
                    res=a*b
                    stack.append(res)
                elif char=="/":
                    res=int(b/a)
                    stack.append(res)
        
        return stack[-1]