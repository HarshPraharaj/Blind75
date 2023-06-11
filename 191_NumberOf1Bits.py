## Shift n by >>

class Solution:
    def hammingWeight(self, n: int) -> int:
        
        one_cnt = 0
        print(n)
        while n > 0:
            dig = n % 2
            # print(dig)
            if dig == 1:
                one_cnt += 1
            n = n >> 1
        return one_cnt
