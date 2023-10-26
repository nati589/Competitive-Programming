class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        items = {}
        for i in range(len(nums)):
            items[nums[i]] = 0
        for i in range(len(nums)):
            items[nums[i]] += 1
        for i in range(len(nums)):
            if items[nums[i]] > 1 :
                return True
            
        return False