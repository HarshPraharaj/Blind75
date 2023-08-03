class Solution:
    def longestPalindrome(self, s: str) -> int:

        dict1 = Counter(s)
        print(dict1)
        max_len = 0

        for k in dict1.keys():
            
            max_len += ((dict1[k] // 2) * 2)

            if dict1[k]%2 == 1 and max_len %2 ==0:
                max_len+=1
        return max_len
