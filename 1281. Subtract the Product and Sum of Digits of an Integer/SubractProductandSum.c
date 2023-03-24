int subtractProductAndSum(int n){
    int sum=0,product=1,modulo;
    while(n>0){
        modulo=n%10;
        sum+=modulo;
        product*=modulo;
        n/=10;
    } 
    return product - sum;
}