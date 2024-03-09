# Minimum Common Value

class Solution(object):
    def getCommon(self, nums1, nums2):
        i = 0
        j = 0
        common = float('inf')
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                common = nums1[i]
                break
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        
        return common if common != float('inf') else -1

solution = Solution()
print(solution.getCommon([1,2,3], [2,4]))