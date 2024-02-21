# Richest Customer Wealth

class Solution(object):
    def maximumWealth(self, accounts):
        max_wealth = 0
        for account in accounts:
            max_wealth = max(max_wealth, sum(account))
        return max_wealth

test = Solution()
print(test.maximumWealth([[1,2,3],[3,2,1]]))