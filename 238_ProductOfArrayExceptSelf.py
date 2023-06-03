## Either create two lists to store product before and after the index vale OR Do a 2 pass and store everything in final list
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        results_list = [1]*len(nums)

        pre = 1
        for i in range(0,len(nums)):
            if i == 0 :
                results_list[i] = pre
            else:
                results_list[i] = pre * nums[i-1]
                pre = results_list[i]
        print(results_list)
        
        post = 1
        for i in range(len(nums)-1,-1,-1):
            if i == len(nums)-1:
                results_list[i] *= post
                post = nums[i]
            else:
                results_list[i]*=post
                post = post*nums[i]
        return results_list
      
      
        # for i in range(0,len(nums)):
        #     if i == 0:
        #         results_list[i] = nums[i]
        #     else:
        #         results_list[i] = nums[i] * results_list[i-1]
        # print(results_list)

        # post_results = [1]*len(nums)
        # for i in range(len(nums),1,-1):
        #     if i == len(nums):
        #         post_results[i-1] = nums[i-1]
        #     else:
        #         post_results[i-1] = post_results[i] * nums[i-1]
        # print(post_results)
