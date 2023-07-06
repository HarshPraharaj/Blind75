class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left = 0
        seen = set()
        max_len = 0
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left = left + 1
            seen.add(s[right])
            max_len = max(max_len, right-left+1)
            print(seen)
        return max_len
        # max_len = 0
        # for right in range(len(s)):
        #     if s[right] in seen:
        #         left = s.find(s[right],left) +1
        #         # left = s.index(s[right]) + 1
        #         # seen.remove(s[right])
        #         substr = s[left:right+1]
        #         max_len = max(max_len,len(substr))
        #     else:
        #         seen.add(s[right])
        #         substr = s[left:right+1]
        #         max_len = max(max_len,len(substr))
        #     print(left)
        #     print(substr)
        # return max_len
