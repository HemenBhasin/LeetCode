# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        real_dummy=ListNode(0)
        real_dummy.next=head
        dummy=real_dummy
        c=head
        while c is not None:
            if c.next is not None and c.val==c.next.val:
                val=c.val
                while c is not None and c.val==val:
                    c=c.next
                dummy.next=c
            else:
                dummy=c
                c=c.next        
        return real_dummy.next      
        