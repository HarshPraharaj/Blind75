## Use Hashmaps to store indices hence avoiding two passes.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dict1 = {}
        final_op = []
        for i, num in enumerate(nums):
            res = target - num
            if res in dict1.keys():
                final_op.append(dict1[res])
                final_op.append(i)
            dict1[num] = i
        print(final_op)
        return final_op
            
