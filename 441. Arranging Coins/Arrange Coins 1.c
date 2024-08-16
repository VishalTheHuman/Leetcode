int arrangeCoins(int n){
    int i=1;
    while (n!=0)
    {
        n=n-i;
        if(n==0)
        {return i;}
        if (n<0)
        {return i-1;}
        i++;
    }
    return i;
}