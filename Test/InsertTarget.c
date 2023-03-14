#include<stdio.h>
int searchInsert(int* nums, int numsSize, int target){
    int index=0;
    for(int i=0;i<numsSize;i++)
    {
        if(nums[i]<target){
            index++;
        }else{
            return index;
        }
    }
    if(index>0){
        return index;
    }
    else{
        return 0;
    }
}
void main(){
    int arr[4]={1,3,5,6};
    printf("%d",searchInsert(arr,4,0));
}