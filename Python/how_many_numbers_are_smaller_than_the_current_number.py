# How Many Numbers Are Smaller Than the Current Number

class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        counts = [0] * 101
        for num in nums:
            counts[num] += 1

        smaller_counts = [0] * len(nums)
        for i in range(len(nums)):
            smaller_counts[i] = sum(counts[:nums[i]])

        return smaller_counts

test = Solution()
print(test.smallerNumbersThanCurrent([8,1,2,2,3]))