class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxNum = 0
        for buy in range(len(prices)):
            for sell in range(buy, len(prices)):
                profit = prices[sell] - prices[buy]
                if profit > maxNum:
                    maxNum = profit         
        return maxNum
                    



        