class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ops=["+","C","D"]
        stack=[]
        for val in operations:
            
            if val=='+':
                stack.append(stack[-1]+stack[-2])
            elif val=="C":
                stack.pop()
            elif val=="D":
                stack.append(2*stack[-1])
            else:
                stack.append(int(val))

        return sum(stack)