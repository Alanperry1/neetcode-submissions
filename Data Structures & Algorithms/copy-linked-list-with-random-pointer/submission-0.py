"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        newNodes={None:None}
        curr=head
        while curr:
                copy=Node(curr.val)
                newNodes[curr]=copy
                curr=curr.next

        curr=head
        while curr:
            copy=newNodes[curr]
            copy.next=newNodes[curr.next]
            copy.random=newNodes[curr.random]
            curr=curr.next

        return newNodes[head]