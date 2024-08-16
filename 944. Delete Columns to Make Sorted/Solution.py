class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        def isSorted(string):
            return string == "".join(sorted(string))
        n = 0
        for i in range(len(strs[0])):
            s = "".join([x[i] for x in strs])
            if not isSorted(s):
                n+=1
        return n