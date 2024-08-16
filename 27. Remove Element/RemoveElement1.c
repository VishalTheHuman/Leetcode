int removeElement(int* nums, int numsSize, int val){
    int count=0;int temp;
    for(int i=0;i<numsSize;i++){
        if(nums[i]==val){
            nums[i]=101;
            count++;
        }          
        for(int j=0;j<numsSize;j++){
            if (nums[i]<nums[j]){
                temp=nums[i];
                nums[i]=nums[j];
                nums[j]=temp;
            }
        }
        if(nums[i]==val){
            nums[i]=101;
            count++;
        }           
    }
    return numsSize-count;
}