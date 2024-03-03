# Find the Difference of Two Arrays

class Solution(object):
    def findDifference(self, nums1, nums2):
        nums1, nums2 = set(nums1), set(nums2)
        return [[num for num in nums1 if num not in nums2], [num for num in nums2 if num not in nums1]]

solution = Solution()
print(solution.findDifference([1,2,3], [2,4,6]))