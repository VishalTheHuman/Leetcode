int reverse(int x){
    if(x>2147483647 || x==-2147483648 ){
        return 0;
    }
    int y=x;
    int sum=0;
    long sum1=0;
    int modulo;
    int flag =0;
    if(x<0){
        flag =1;
        y=y/-1;
    }
    while(y>0){
        modulo=y%10;
        sum1=sum1*10+modulo;
        if(sum1>2147483647){
        return 0;}
        sum=sum*10 + modulo;
        y=y/10;
    }
    if(flag==1){
        return -1*(sum);
    }
    return sum;
}