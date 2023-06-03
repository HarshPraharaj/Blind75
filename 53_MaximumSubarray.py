## keep an eye out for negative numbers. if they bring the overall sum to 0, reset it.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        max_sub = nums[0]
        curSum = 0

        for num in nums:
            if curSum < 0:
                curSum = 0
            curSum += num
            max_sub = max(max_sub,curSum)

        return max_sub
