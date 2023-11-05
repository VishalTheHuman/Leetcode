class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        winner = arr[0]
        count = 0
        for i in range(1,len(arr)):
            if arr[i]>winner:
                count = 1
                winner = arr[i]
            else:
                count+=1
            if count==k:
                return winner
        return winner
