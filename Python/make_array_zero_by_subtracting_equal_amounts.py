# Make Array Zero by Subtracting Equal Amounts

class Solution(object):
    def minimumOperations(self, nums):
        return len(set(nums) - {0})
        
solution = Solution()
print(solution.minimumOperations([59, 5, 51, 97, 40, 56, 24, 79, 57, 29, 15, 25, 14, 5, 36, 96, 21, 83, 17, 22, 11, 49, 84, 32, 62, 44, 1, 64, 69, 15, 78, 51, 96, 47, 25, 68, 82, 70, 80, 99, 6, 78, 38, 64, 95, 47, 24, 99, 50, 39, 40, 37, 66, 80, 56, 49, 52, 94, 58, 17, 48, 98, 65, 27, 87, 82, 47, 95, 67, 84, 44, 42, 96, 5, 50, 15, 34, 92, 34, 59, 18, 28, 4, 39, 77, 51, 86, 1, 90, 19, 25, 96, 100, 62, 4, 79, 55, 93, 81, 60]))