class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1
        area = float("-inf")
        while i < j:
            curr = min(heights[i], heights[j]) * (j - i)
            area = max(area, curr)

            if heights[i] > heights[j]:
                j -= 1
            else:
                i += 1
        
        return area