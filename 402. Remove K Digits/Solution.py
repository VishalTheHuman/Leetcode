class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for idx, val in enumerate(num):
            if k == 0:
                stack.extend(list(num[idx:]))
                break
            
            if stack and stack[-1] > val:
                while stack and k > 0 and stack[-1] > val:
                    k-=1
                    stack.pop()

            stack.append(val)
        
        while stack and stack[0]=="0":
            stack.pop(0)

        if k: 
            stack = stack[:-k]

        return "".join(stack) if stack else "0"
