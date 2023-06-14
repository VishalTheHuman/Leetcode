class Solution {
    public int minOperations(String[] logs) {
        Stack<String> folder = new Stack<>();
        for(int i=0;i<logs.length;i++){
            if(logs[i].equals("../") && folder.size()>=1){
                folder.pop();
            }else if(!logs[i].equals("./") && !logs[i].equals("../")){
                folder.push(logs[i]);
            }
        }
        return folder.size();
    }
}

/*
class Solution {
    public int minOperations(String[] logs) {
        Stack<String> folder = new Stack<>();
        for(int i=0;i<logs.length;i++){
            if(logs[i].equals("../") && folder.size()>=1) folder.pop();
            else if(!logs[i].equals("./") && !logs[i].equals("../")) folder.push(logs[i]);
        }
        return folder.size();
    }
}
 */