int romanToInt(char * s){
    int size=strlen(s);
    int sum=0;
    for(int i=0;i<size;i++){
        switch (s[i])
        {
        case 'I':
            if(s[i+1]=='X' ||s[i+1]=='V' && i<size-1){
                sum-=1;
            }
            else{
                sum+=1;
            }
            break;
        case 'V':
            sum+=5;
            break;
        case 'X':
            if(s[i+1]=='L' ||s[i+1]=='C' && i<size-1){
                sum-=10;
            }
            else{
                sum+=10;
            }
            break;
        case 'L':
            sum+=50;
            break;
        case 'C':
            if(s[i+1]=='D' ||s[i+1]=='M' && i<size-1){
                sum-=100;
            }
            else{
                sum+=100;
            }
            break;
        case 'D':
            sum+=500;
            break;
        case 'M':
            sum+=1000;
            break;
        default:
            break;
        }
    }
    return sum;
}
