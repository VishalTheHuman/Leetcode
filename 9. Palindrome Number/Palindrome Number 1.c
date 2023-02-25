bool isPalindrome(int x){
    unsigned long int ori=x;unsigned long int y=0; unsigned long int n;
    while (x>0){
        n=x;
        x=n%10;
        y=y*10+x;
        x=n/10;}
    if(y==ori)
    {return true;}
    else { return false;}
}