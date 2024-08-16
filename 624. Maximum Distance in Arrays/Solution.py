class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        maxInt = [[-float("inf"),None], [-float("inf"), None]]
        minInt = [[float("inf"), None], [float("inf"), None]]
        for i in range(len(arrays)):
            if arrays[i][0] < minInt[0][0]:
                minInt[1] = minInt[0]
                minInt[0] = [arrays[i][0], i]
            elif arrays[i][0] < minInt[1][0]:
                minInt[1] = [arrays[i][0], i]
            
            if arrays[i][-1] > maxInt[0][0]:
                maxInt[1] = maxInt[0]
                maxInt[0] = [arrays[i][-1], i]
            elif arrays[i][-1] > maxInt[1][0]:
                maxInt[1] = [arrays[i][-1], i]
        
        maxDistance = 0
        for i in range(2):
            for j in range(2):
                if maxInt[i][1]!=minInt[j][1]:
                    if maxInt[i][0] < 0 and minInt[j][0] < 0:
                        maxDistance = max(maxDistance, abs(minInt[j][0] - maxInt[i][0]))
                    else:
                        maxDistance = max(maxDistance, abs(maxInt[i][0] - minInt[j][0]))
        return maxDistance
