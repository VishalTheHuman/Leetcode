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
    public int getDecimalValue(ListNode head) {
        int count = 0;
        ListNode temp = head;
        while(temp!=null){
            count+=1;
            temp=temp.next;
        }
        int[] arr = new int[count];
        temp = head;
        int ind = count-1;
        while(temp!=null){
            arr[ind] = temp.val;
            ind-=1;
            temp = temp.next;
        }
        int sum = 0;
        for(int i=0;i<count;i++){
            sum+=(arr[i] * (int) Math.pow(2,i));
        }
        return sum;
    }
}