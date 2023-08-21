class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        count = 0
        for x in hours:
            if x>=target:
                count+=1
        return count