/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        PriorityQueue<ListNode> pq=new PriorityQueue<>((a, b) -> a.val - b.val);//sort them in ascending order
        for (ListNode node : lists){
            if (node!=null){
                pq.add(node);
            }
        }
        ListNode dummy= new ListNode(0);
        ListNode tail = dummy; // Use tail to build the new list
        while (!pq.isEmpty()){
            ListNode curr=pq.poll();
            
            tail.next = curr;
            tail = tail.next;

            if (curr.next!=null){
                pq.add(curr.next);
            }
        }
        return dummy.next; //Return the merged list (skipping the dummy head)
    }
}