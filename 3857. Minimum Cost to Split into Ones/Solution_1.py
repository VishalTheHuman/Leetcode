class Solution:
    def minCost(self, n: int) -> int:
        store = defaultdict(int)
        score = 0 

        def recurse(num): 
            if num == 1:
                return 0
            a = b = 0
            if store[num] == 0:
                s = float(inf)
                for i in range(1,int(math.sqrt(num))+1):
                    ta, tb = num-i, i
                    if s > ta*tb : 
                        a,b = ta,tb
                        s = ta*tb
                store[num] = s + recurse(a) + recurse(b)
            return store[num]

        return recurse(n)
