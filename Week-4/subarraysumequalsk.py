from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = defaultdict(int)
        s = 0
        dic[0] = 1
        res = 0
        for n in nums:
            s += n
            if s - k in dic:
                res += dic[s - k]
            dic[s] += 1
        return res
