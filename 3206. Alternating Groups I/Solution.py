class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        count = 0
        l = len(colors)
        for i in range(l):
            if colors[i]!=colors[(i+1)%l] and colors[(i+1)%l]!= colors[(i+2)%l]:
                count+=1
        return count
