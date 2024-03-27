# Subarray Product Less Than K

class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        if k <= 1:
            return 0

        left, right, product, count = 0, 0, 1, 0
        n = len(nums)

        while right < n:
            product *= nums[right]
            while product >= k:
                product //= nums[left]
                left += 1
            count += 1 + (right - left)
            right += 1

        return count
    
solution = Solution()
print(solution.numSubarrayProductLessThanK([10,5,2,6], 100))