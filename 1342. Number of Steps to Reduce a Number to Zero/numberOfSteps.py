class Solution:
    def numberOfSteps(self, num: int) -> int:
        flag=0
        while num>0 :
            if(num%2==1):
                num-=1
                flag+=1
                continue
            num/=2
            flag+=1
        return flag;