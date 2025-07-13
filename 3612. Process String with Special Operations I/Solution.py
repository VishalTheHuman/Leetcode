class Solution:
    def processStr(self, s: str) -> str:
        result = []
        operations = set(["*","#","%"])
        for char in s: 
            if char in operations: 
                if char == "*": 
                    if result: 
                        result.pop()
                elif char == "#": 
                    result.extend(result)
                else: 
                    result.reverse()
            else: 
                result.append(char)
        
        return "".join(result)
