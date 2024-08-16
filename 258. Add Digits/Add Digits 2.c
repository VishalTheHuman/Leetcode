int addDigits(int num){
    int x=num,y;
    if(num==0)
    {return num;}
    do
    {
        y=0; num=x;
        while (x!=0)
        {
            x=x%10;
            y+=x;
            x=num/10;
            num=num/10;
        }

        x=y;
    } while (y>=10);
    return y;
}