class Solution {
    public int findGCD(int[] nums) {
        int smallest = nums[0];
        int largest = nums[0];
        for(int i=0;i<nums.length;i++){
            if(nums[i]>largest){
                largest = nums[i];
            }else if(nums[i]<smallest){
                smallest = nums[i];
            }
        }
        int gcd = 1;
        int i=2;
        while(i<=smallest){
            if(i%2==0 && i!=2){
                i++;
                continue;
            }
            if(largest%i==0 && smallest%i==0){
                gcd*=i;
                largest/=i;
                smallest/=i;
            }else{
                i++;
            }
        }
        return gcd;
    }
}