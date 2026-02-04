class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        def check(): 
            temp = sorted(count.items(), 
            reverse = True, 
            key = lambda y : (y[1],y[0]))[:x]

            return sum(
                list(map(lambda y : y[0]*y[1], temp))
            )

        count = defaultdict(int)
        answer = [] 
        for i in range(k): 
            count[nums[i]] += 1
        answer.append(check())
                
        for i in range(k, len(nums)): 
            if count[nums[i-k]] == 1:
                del count[nums[i-k]]
            else:
                count[nums[i-k]] -=1 
            count[nums[i]] += 1
            answer.append(check())
        return answer
