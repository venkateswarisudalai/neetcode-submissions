class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        left = 0
        right = len(heights)-1
        max_len = 0

        while(left<right):

            area = (right-left)*min(heights[left],heights[right])
            max_len = max(max_len,area)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max_len