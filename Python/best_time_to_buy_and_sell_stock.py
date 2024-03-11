# Best Time to Buy and Sell Stock

class Solution(object):
    def maxProfit(self, prices):
        min_price = prices[0]
        max_profit = 0
        
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)

        return max_profit

solution = Solution()
print(solution.maxProfit([7,1,5,3,6,4]))