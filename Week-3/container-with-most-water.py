class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        length = 0
        area = 0

        while left < right:
            if height[left] > height[right]:
                length = height[right]
            else:
                length = height[left]
            if area < (right - left) * length:
                area = (right - left) * length
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return area
