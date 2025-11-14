class Solution:
    def simplifyPath(self, path: str) -> str:
        new_path = []
        curr = ""

        def validate(): 
            nonlocal curr
            if curr == "..":
                if new_path: 
                    new_path.pop()
            elif curr != "." and curr: 
                new_path.append(curr)
            curr = ""

        for c in path: 
            if c == "/":
                validate()
            else:
                curr += c
        
        validate()
        
        return "/" + "/".join(new_path)
