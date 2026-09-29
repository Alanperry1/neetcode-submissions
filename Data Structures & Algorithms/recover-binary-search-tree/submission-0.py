# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        res=[]
        def dfs(node):
            if not node:
                return 
            dfs(node.left)
            res.append(node)
            dfs(node.right)
        dfs(root)
        node1,node2=None,None
        for i in range(len(res)-1):
            if res[i].val>res[i+1].val:
                node2=res[i+1]
                if node1 is None:
                    node1=res[i]
                else:
                    break
        node1.val,node2.val=node2.val,node1.val

