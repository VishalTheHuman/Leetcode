int hammingWeight(uint32_t n) {
    int count=0,y;
    for(int i=0;i<32;i++)
    {
        y=n%2;
        if(y==00000000000000000000000000000001)
        {count++;}
        n=n/2;
    }
    return count;
}