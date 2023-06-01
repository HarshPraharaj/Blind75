## Solution 1 :- Two pointers left and right. 
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        max_profit = 0

        if len(prices)<=1:
            return 0

        for index,price in enumerate(prices):
            print(l,r)
            if r == len(prices):
                    break
            if prices[l] > prices[r]:
                l = r
                r+=1
            
            else:
                profit = prices[r] - prices[l]
                if profit > max_profit:
                    max_profit = profit
                r+=1
        return max_profit
      
## Solution 2 :- Greedy Approach
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_buy_price = 100000

        for price in prices:
            min_buy_price = min(min_buy_price,price)
            max_profit = max(max_profit, price - min_buy_price)

        return max_profit
