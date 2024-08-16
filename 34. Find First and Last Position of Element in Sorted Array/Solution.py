class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        pos = [-1,-1]
        i = 0
        j = len(nums)-1
        while i<=j:
            mid = (i+j)//2
            if nums[mid]==target:
                pos[0] = pos[1] = mid
                i = j = mid
                break
            elif nums[mid] < target:
                i = mid+1
            else:
                j = mid-1
        if pos[0] == pos[1] == -1:
            return pos
        while True:
            count = 0
            if i > 0:
                if nums[i-1]==target:
                    i-=1
                    count+=1
            if j < len(nums)-1:
                if nums[j+1]==target:
                    j+=1
                    count+=1
            if count==0:
                pos[0] = i
                pos[1] = j
                break
        return pos