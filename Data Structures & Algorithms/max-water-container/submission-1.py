class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        maxAmount = 0
        while left < right:
            area = (right-left) * min(heights[right], heights[left])
            if area > maxAmount:
                maxAmount = area
            if heights[right] > heights[left]:
                left += 1
            else:
                right -= 1
        return maxAmount
        