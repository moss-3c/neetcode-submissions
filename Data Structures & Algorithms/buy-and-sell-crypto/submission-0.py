class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # edge case
        if len(prices) == 1:
            return 0 # can't sell lol

        maxProfit = 0
        bestBuy = prices[0]

        for i in range(1, len(prices)):
            profit = prices[i] - bestBuy
            if profit > maxProfit:
                maxProfit = profit

            if prices[i] < bestBuy:
                bestBuy = prices[i]
        
        return maxProfit