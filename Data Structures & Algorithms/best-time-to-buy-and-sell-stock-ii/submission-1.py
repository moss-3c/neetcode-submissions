class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        tot = 0
        i = 0
        while (i < len(prices) - 1):
            # if increasing stock price
            change = prices[i + 1] - prices[i]
            if prices[i + 1] > prices[i]:
                tot += change
            
            i += 1
        
        return tot
