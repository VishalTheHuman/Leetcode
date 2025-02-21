/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class FindElements {
    HashSet<Integer> seen = new HashSet<>(); 
    public FindElements(TreeNode root) {
        root.val = 0; 
        seen.add(0); 
        traverse(root);
    }

    public void traverse(TreeNode root){
        if (root.left!=null){
            root.left.val = 2*root.val+1;
            seen.add(root.left.val); 
            traverse(root.left); 
        }

        if (root.right!=null){
            root.right.val = 2*root.val+2;
            seen.add(root.right.val); 
            traverse(root.right); 
        }
    }
    
    public boolean find(int target) {
        return seen.contains(target); 
    }
}

/**
 * Your FindElements object will be instantiated and called as such:
 * FindElements obj = new FindElements(root);
 * boolean param_1 = obj.find(target);
 */
