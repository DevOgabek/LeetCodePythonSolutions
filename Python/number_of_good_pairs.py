# Number of Good Pairs

class Solution(object):
    def numIdenticalPairs(self, nums):
        n = len(nums)
        count = 0
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] == nums[j]:
                    count += 1
        return count

test = Solution()
print(test.numIdenticalPairs([1,2,3,1,1,3]))