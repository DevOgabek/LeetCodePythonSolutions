# Remove Element

class Solution(object):
    def removeElement(self, nums, val):
        left, right = 0, len(nums) - 1
        
        while left <= right:
            if nums[left] == val:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
            else:
                left += 1
        
        return left
    
solution = Solution()
print(solution.removeElement([3,2,2,3], 3))
