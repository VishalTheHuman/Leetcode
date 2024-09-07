class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if name[0]!=typed[0] : return False
        ptr = itr = 0
        while ptr < len(name) and itr < len(typed): 
            if name[ptr] == typed[itr]:
                ptr += 1
            if name[ptr-1]!=typed[itr]:
                return False
            itr += 1
        while itr < len(typed) and typed[itr] == name[ptr-1]:
            itr += 1
        return ptr == len(name) and len(typed) == itr
