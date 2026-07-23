# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        while head is not None and head.val==val:
            head=head.next
        c=head
        while c is not None and c.next is not None:
            if c.next.val==val:
                c.next=c.next.next
            else:
                c=c.next
        return head            
        
        