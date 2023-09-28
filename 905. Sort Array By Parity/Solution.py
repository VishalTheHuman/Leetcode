class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        lp, rp = 0, len(nums)-1
        while lp<rp:
            if nums[lp]%2 == 1:
                while nums[rp]%2!=0 and lp<rp:
                    rp-=1
                nums[rp],nums[lp] = nums[lp],nums[rp]
                rp-=1
            else:
                lp+=1
        return nums