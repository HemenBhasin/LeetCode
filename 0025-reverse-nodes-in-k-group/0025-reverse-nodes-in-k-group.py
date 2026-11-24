# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        if not head or k==1:
            return head
        n=0
        curr=head
        while curr:
            n+=1
            curr=curr.next

        temp = ListNode(0, head)
        prev = temp
        curr = head

        for i in range(1, (n // k) * k + 1):
            if i % k == 0:
                prev = curr
                curr = curr.next
            else:
                nxt = curr.next
                curr.next = nxt.next
                nxt.next = prev.next
                prev.next = nxt

        return temp.next   


        