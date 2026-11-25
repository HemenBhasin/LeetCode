# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        if not head:
            return head

        dummy=ListNode(0)
        dummy.next=head
        curr=dummy.next
        prev=dummy
        for i in range(1,left):
            curr=curr.next
            prev=prev.next

        for i in range(right-left):
            temp=curr.next
            curr.next=temp.next
            temp.next=prev.next
            prev.next=temp
        return dummy.next    



