class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) > 12:
            return []

        result, curr = [], []

        def backtrack(idx, remain = 3, num = None):
            if idx >= len(s):
                if remain == 0 and num is not None:
                    curr.append(str(num))
                    result.append("".join(curr))
                    curr.pop()
                return

            num = (0 if num is None else num*10) + int(s[idx])
            
            if 0 <=num<=255:
                if num > 0:
                    backtrack(idx+1, remain, num)
                curr.append(str(num))
                if remain:
                    curr.append(".")
                    backtrack(idx+1, remain-1)
                    curr.pop()
                elif (idx+1)==len(s) and num ==0:
                    result.append("".join(curr))
                curr.pop()
            
        backtrack(0)

        return result
