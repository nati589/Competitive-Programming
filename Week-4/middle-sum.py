class Solution:
    def pivotIndex(self, nums):
        leftSum = 0
        rightSum = 0
        for x in range(len(nums)):
            rightSum += nums[x]
        for x in range(len(nums)):
            rightSum -= nums[x]
            if leftSum == rightSum:
                return x
            else:
                if x == len(nums) - 1:
                    return -1
                leftSum += nums[x]