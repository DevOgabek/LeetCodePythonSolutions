# Find Common Elements Between Two Arrays

class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        set1 = set(nums1)
        set2 = set(nums2)
        
        count1 = sum(1 for num in nums1 if num in set2)
        
        count2 = sum(1 for num in nums2 if num in set1)
        
        return [count1, count2]

solution = Solution()
print(solution.findIntersectionValues([4,3,2,3,1], [2,2,5,2,3,6]))