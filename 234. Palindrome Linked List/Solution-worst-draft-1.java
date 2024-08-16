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
    public boolean isPalindrome(ListNode head) {
        List<Integer> ret = new ArrayList<>();
        ListNode temp = head;
        int count=0;
        while(temp!=null){
            ret.add(temp.val);
            temp = temp.next;
            count+=1;
        }
        if(count%2==1){
            ret.remove((int)(count/2));
        }
        count/=2;
        while(count>=0){
            if(ret.size()!=0){
                if(ret.get(0)==ret.get(ret.size()-1)){
                    ret.remove(0);
                    ret.remove(ret.size()-1);
                }
            }
            count-=1;
        }
        if(ret.size()==0){
            return true;
        }
        return false;
    }
}