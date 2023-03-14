int missingNumber(int* nums, int numsSize){
    int i=0, index=0, count=0;
    while(i<numsSize){
        if(nums[i]==i+1){
            i++;
        }else if(nums[i]==0){
            count++;
            index=i;
            i++;
        }else{
            swap(nums,i,nums[i]-1);
        }
    }
    if(count==0){
        return 0;
    } else{
        return index+1;
    }
}
void swap(int *a, int i,int j){
    int temp = a[i];
    a[i]=a[j];
    a[j]=temp;
}