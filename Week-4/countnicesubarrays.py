class Solution:
    def numberOfSubarrays(self, nums, k):
        def atMostK(k):
            res = i = 0
            for j in range(len(nums)):
                k -= nums[j] % 2
                while k < 0:
                    k += nums[i] % 2
                    i += 1
                res += j - i + 1
            return res
        return atMostK(k) - atMostK(k - 1)