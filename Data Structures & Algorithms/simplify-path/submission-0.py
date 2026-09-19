class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        idv=path.split("/")

        for p in idv:
            if p=="..":
                if stack:
                    stack.pop()
            elif p!="" and p!=".":
                stack.append(p)


        return "/" + "/".join(stack)