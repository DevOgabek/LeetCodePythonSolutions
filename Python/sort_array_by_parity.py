# Sort Array By Parity

class Solution(object):
    def sortArrayByParity(self, nums):
        left = 0
        right = len(nums) - 1
        
        while left < right:
            if nums[left] % 2 == 0:
                left += 1
            elif nums[right] % 2 != 0:
                right -= 1
            else:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        
        return nums
    
solution = Solution()
print(solution.sortArrayByParity([3,1,2,4]))