## Brute Force to check all combinations or use left and right pointer to calculate area at each step and then increment/decrement l/r pointer based on whichever is greater

class Solution:
    def maxArea(self, height: List[int]) -> int:

        max_area = 0
        l = 0
        r = len(height)-1

        while l < r:
            cur_area = min(height[l],height[r]) * (r-l)
            max_area = max(max_area, cur_area)

            if height[l] > height[r]:
                r = r - 1
            else:
                l = l + 1

        return max_area
