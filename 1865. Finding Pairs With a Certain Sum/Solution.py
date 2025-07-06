class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums2 = nums2
        self.s1 = defaultdict(int)
        self.s2 = defaultdict(int)

        for x in nums1: 
            self.s1[x] += 1
            
        for x in nums2: 
            self.s2[x] += 1

    def add(self, index: int, val: int) -> None:
        self.s2[self.nums2[index]] -= 1
        if self.s2[self.nums2[index]] == 0: 
            del self.s2[self.nums2[index]]
        self.nums2[index] += val
        self.s2[self.nums2[index]] += 1

    def count(self, tot: int) -> int:
        answer = 0
        for x in self.s1.keys(): 
            if x >= tot: 
                continue
            answer += self.s1[x] * self.s2[tot - x]
        return answer

# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
