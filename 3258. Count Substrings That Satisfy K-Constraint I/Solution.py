class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        ones = [0]
        zeros = [0]
        for x in s:
            ones.append(ones[-1]+(x=="1"))
            zeros.append(zeros[-1]+(x=="0"))
        
        count = 0    
        
        for i in range(len(s)):
            for j in range(i,len(s)):
                if (zeros[j+1] - zeros[i]) <= k or (ones[j+1]-ones[i]) <= k:
                    count += 1
        
        return count
            

