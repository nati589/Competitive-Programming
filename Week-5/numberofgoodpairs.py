class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        output = 0
        res = {}
        for item in nums:    
            if item in res:
                res[item] = 1 + res.get(item, 0)
            else:
                res[item] = 1
                
        for item in res.values():
            output += item * (item - 1) / 2 
        return int(output)
       