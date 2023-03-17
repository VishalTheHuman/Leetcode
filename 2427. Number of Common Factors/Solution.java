class Solution {
    public int commonFactors(int a, int b) {
    int common =1,facthelp;
    if(a>b){
        facthelp=b;
    }else{
        facthelp =a;
    }
    for(int i=2;i<=facthelp;i++){
        if(a%i==0 && b%i==0){
            common++;
        }
    }
    return common;
    }
}