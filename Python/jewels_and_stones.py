# Jewels and Stones

class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        count = 0
        for jewel in jewels:
            for stone in stones:
                count += stone.count(jewel)
        return count

test = Solution()
print(test.numJewelsInStones("aA", "aAAbbbb"))