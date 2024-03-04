# Final Prices With a Special Discount in a Shop

class Solution(object):
    def finalPrices(self, prices):
        stack = []
        for i, price in enumerate(prices):
            while stack and prices[stack[-1]] >= price:
                prices[stack.pop()] -= price
            stack.append(i)
        return prices

solution = Solution()
print(solution.finalPrices([8,4,6,2,3]))