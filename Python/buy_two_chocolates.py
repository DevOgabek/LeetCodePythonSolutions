# Buy Two Chocolates

class Solution(object):
    def buyChoco(self, prices, money):
        prices.sort()
        cheapest_chocolates = sum(prices[:2])
        difference = abs(cheapest_chocolates - money) if cheapest_chocolates <= money else money
        return difference
    
solution = Solution()
print(solution.buyChoco([1,2,2], 3))