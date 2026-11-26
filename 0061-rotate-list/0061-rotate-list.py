# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        if not head:
            return head
        n = 1
        curr = head
        while curr.next:
            n += 1
            curr = curr.next
        k=k%n
        
        curr.next = head
        temp=head
        for i in range(n-k-1):
            temp=temp.next
        rs=temp.next   
        temp.next=None


        return rs
        