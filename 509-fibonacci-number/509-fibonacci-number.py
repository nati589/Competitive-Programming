class Solution:
    def fib(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 0:
            return 0
        
        p1, p2 = 1, 0
        output = 0
        for i in range(2, n+ 1):
            output = p1 + p2
            p2 = p1
            p1 = output
        
        return output