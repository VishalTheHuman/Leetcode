class Solution:
    def lastVisitedIntegers(self, words: List[str]) -> List[int]:
        ret = []
        nums = []
        prev = 0
        for x in words:
            if x == "prev":
                prev+=1
                if prev > len(nums):
                    ret.append(-1)
                else:
                    ret.append(nums[prev-1])
            else:
                nums.insert(0,int(x))
                prev = 0
        return ret