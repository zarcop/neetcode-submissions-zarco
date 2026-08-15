class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        
        left = 0 
        right = 1
        minPrice = float('inf')
        maxprofit = 0
        while left < len(prices) - 1:
            if prices[left] < minPrice:
                minPrice = prices[left]
                while right < len(prices):
                    profit = prices[right] - prices[left]
                    maxprofit = max(profit, maxprofit)
                    right += 1
            else:
                left += 1
                right = left + 1
        return maxprofit
                    

            

        
            
        