#include<stdio.h>

void reverseString(char* s, int sSize){
    for(int i=0;i<sSize/2;i++)
    {
        int temp=s[i];
        s[i]=s[sSize-1-i];
        s[sSize-1-i]=temp;
    }
}

void disp(char *s,int size){
    for(int i=0;i<size;i++){
        printf("%c ",s[i]);
    }
}
void main(){
    char arr[]={'d','e','n','m','a','r','k','s'};
    reverseString(arr,8);
    disp(arr,8);
}