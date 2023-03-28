class Solution {
    public boolean isThree(int n) {
        int k=1;
        for(int i=1;i<=n/2;i++){
            if(n%i==0){
                k++;
            }
            if(k>3){
                return false;
            }
        }
        if(k==3){
            return true;
        }
        return false;
    }
}