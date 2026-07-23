# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        l=r=head
        for i in range(k-1):
            l=l.next
        temp=l 
        while l.next:
            r=r.next
            l=l.next
        temp.val,r.val=r.val,temp.val
        return head
        