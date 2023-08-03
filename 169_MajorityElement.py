class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict1 = Counter(nums)

        largest_key = max(dict1, key=dict1.get)

        return largest_key
