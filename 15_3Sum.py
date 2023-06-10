## Take the idea of sorting list and using two pointers from 2Sum II .

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums = sorted(nums)
        final_res = []

        for index,num in enumerate(nums):
            if index > 0 and nums[index-1] == num:
                continue
            l = index + 1
            r = len(nums) - 1

            while l < r:
                threeSum = num + nums[r] + nums[l]
                if threeSum > 0 :
                    r = r - 1
                elif threeSum < 0 :
                    l = l + 1
                else:
                    final_res.append([num,nums[l],nums[r]])
                    l = l + 1
                    while nums[l] == nums[l-1] and l < r:
                        l = l + 1

        return final_res
