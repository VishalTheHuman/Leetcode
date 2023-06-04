class Solution {
    public int diagonalPrime(int[][] nums) {
        List<Integer> ret = new ArrayList<>();
        int j = nums.length-1;
        for(int i = 0;i<nums.length;i++){
            ret.add(nums[i][i]);
            ret.add(nums[j][i]);
            j--;
        }
        return largest(ret);
    }
    public int largest(List<Integer> list){
        int large = list.get(0);
        Collections.sort(list);
        int i=list.size()-1;
        while(i>=0){
            if(isPrime(list.get(i))){
                return list.get(i);
            }
            i--;
        }
        return 0;
    }
    public boolean isPrime(int num){
        if(num==1){
            return false;
        }
        for(int i=2;i*i<=num;i++){
            if(num%i==0){
                return false;
            }
        }
        return true;
    }
}