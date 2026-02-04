class Solution:
    def minLengthAfterRemovals(self, s: str) -> int:
        stk = []
        for x in s: 
            if stk: 
                top = stk[-1]
                if (top == a and x == b) or (top == b and x == a) : 
                    stk.pop()
                else: 
                    stk.append(x)
            else: 
                stk.append(x)
        return len(stk)
