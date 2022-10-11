class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if 0 not in nums:
            return
        p_zero=nums.index(0)
        p_n_zero=0
        while p_n_zero<len(nums) and p_zero<len(nums):
            p_zero=nums.index(0)
            if nums[p_zero]==0 and nums[p_n_zero]!=0 and p_zero<p_n_zero:
                nums[p_zero],nums[p_n_zero]=nums[p_n_zero],nums[p_zero]
                p_n_zero+=1
            elif nums[p_n_zero]==0:
                p_n_zero+=1
            else:
                p_n_zero+=1          
                
                