class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        left = 0
        dict1 = {}
        max_len = 0
        for right,char in enumerate(s):
            if char in dict1.keys():
                dict1[char]+=1
            else:
                dict1[char] = 1 
            print(char)
            print(dict1)
            
            if (right-left+1) - max(dict1.values()) > k:
                dict1[s[left]] -= 1
                left = left+1
                
            max_len = max(right- left + 1, max_len)
        
        return max_len
