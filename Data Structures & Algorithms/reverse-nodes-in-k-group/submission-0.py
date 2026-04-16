# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #Lets get the kth Node
        current,count=head,0
        while current and count<k:
            current=current.next
            count+=1
        if count<k:
            return head

        #reverse k-group
        curr,prev=head,None
        for _ in range(k):
            new_node=curr.next
            curr.next=prev
            prev=curr
            curr=new_node


        head.next=self.reverseKGroup(current,k)
        return prev