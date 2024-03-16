# Contiguous Array

class Solution(object):
    def findMaxLength(self, nums):
        max_length = 0
        sum_map = {0: -1}
        count = 0
        
        for i, num in enumerate(nums):
            if num == 0:
                count -= 1
            else:
                count += 1
                
            if count in sum_map:
                max_length = max(max_length, i - sum_map[count])
            else:
                sum_map[count] = i
        
        return max_length
    
solution = Solution()
print(solution.findMaxLength())