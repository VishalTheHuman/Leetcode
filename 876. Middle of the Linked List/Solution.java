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
    public ListNode middleNode(ListNode head) {
        ListNode temp = head;
        int count = 0;
        while(temp!=null){
            count+=1;
            temp = temp.next;
        }
        int mid = (int)Math.ceil(count/2);
        temp = head;
        count = 0;
        while(count!=mid){
            count+=1;
            temp=temp.next;
        }
        return temp;
    }
}