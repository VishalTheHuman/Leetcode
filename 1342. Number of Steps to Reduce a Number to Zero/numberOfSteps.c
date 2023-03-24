int numberOfSteps(int num){
    int flag=0;
    while(num>0){
        if(num%2==1){
            num-=1;
            flag++;
            continue;
        }
        num/=2;
        flag++;
    }
    return flag;
}