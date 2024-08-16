class Solution {
    public int xorOperation(int n, int start) {
    int sum=0;
    int i=start;
    int flag=0;
    while(flag<n)
    {
        sum^=i;
        i+=2;
        flag++;
    }
    return sum;
    }
}