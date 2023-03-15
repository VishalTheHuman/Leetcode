#include<stdio.h>
#include<stdbool.h>
int search(int* nums, int numsSize, int target){
    int i=0;
    while(true){
        if(nums[i]==target){
            return i;
        }
        if(target<(numsSize+i)/2){
            i=numsSize/2;
        }
    }
}
void main(){
    int arr[100];
    for(int i=0;i<100;i++)
    {
        arr[i]=i-20;
    }
    int a =search(arr,100,34);
    printf("%d",a);
}