class Solution:
    def recurse(self, n):
        return n / 4
    def isPowerOfFour(self, n: int) -> bool:
        while n > 1:
            n = self.recurse(n)
        if n == 1:
            return True
        else: 
            return False 