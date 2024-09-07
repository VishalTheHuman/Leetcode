class Solution:
    def thousandSeparator(self, n: int) -> str:
        n = str(n)
        result = ".".join([n[i:i+3] for i in range(len(n)%3, len(n), 3)])
        if len(n)%3:
            result = n[:(len(n)%3)] + ("." + result if result else "")
        return result
