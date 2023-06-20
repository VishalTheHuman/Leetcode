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
    public ListNode mergeNodes(ListNode head) {
        int count = 0;
        ListNode ret = new ListNode();
        ListNode temp = new ListNode();
        ret = temp;
        while(head!=null){
            if(head.val==0){
                if(temp.val==0){
                    temp.val = count;
                }else{
                    ListNode t = new ListNode();
                    t.val = count;
                    temp.next = t;
                    temp = temp.next;
                }
                count=0;
            }else{
                count+=head.val;
            }
            head = head.next;
        }
        return ret;
    }
}