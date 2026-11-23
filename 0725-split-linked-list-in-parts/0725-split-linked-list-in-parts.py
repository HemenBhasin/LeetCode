# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: ListNode | None, k: int) -> list[ListNode | None]:
        n=0
        curr=head
        while curr:
            n+=1
            curr=curr.next

        part_size=n//k
        cache=n%k
        rs=[]
        curr=head
        for i in range(k):
            rs.append(curr)
            curr_part_size=part_size + 1 if cache>0 else part_size
            cache-=1
            for j in range(curr_part_size-1):
                curr=curr.next
            if curr:
                curr.next, curr= None , curr.next

        return rs        