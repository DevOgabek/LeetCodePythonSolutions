# Number of Arithmetic Triplets

class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        count = 0
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if nums[j] - nums[i] == diff and nums[k] - nums[j] == diff:
                        count += 1
        return count

test = Solution()
print(test.arithmeticTriplets([0,1,4,6,7,10], 3))