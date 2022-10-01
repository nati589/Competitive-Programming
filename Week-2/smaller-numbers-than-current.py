class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        x = []
        for num in nums:
            sum = 0
            for check in nums:
                if check < num:
                    sum += 1
            x.append(sum)
        return x
