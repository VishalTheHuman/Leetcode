class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ls = []
        ptr = 0
        for i in range(1,n+1):
            if ptr>=len(target):
                break
            if i==target[ptr]:
                ls.append("Push")
                ptr+=1
            else:
                ls+=["Push","Pop"]
        return ls
