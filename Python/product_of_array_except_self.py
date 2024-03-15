# Product of Array Except Self

class Solution(object):
    def productExceptSelf(self, nums):
        total_product = 1
        for num in nums:
            total_product *= num
        
        result = []
        
        for num in nums:
            result.append(total_product // num)
        
        return result
    
solution = Solution()
print(solution.productExceptSelf([1,2,3,4]))