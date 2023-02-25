int hammingWeight(uint32_t n) {
    uint32_t num = n;
    int k = 2;
    int count=0;
    int y=0;
    for(int i=0;i<32;i++)
    {
        y=num%k;
        if(y==00000000000000000000000000000001)
        {count++;}
        num=num/k;
    }
    return count;
}