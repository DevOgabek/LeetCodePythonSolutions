# Permutations

class Solution(object):
    def permute(self, nums):
        def backtrack(start):
            if start == len(nums):
                permutations.append(nums[:])
            else:
                for i in range(start, len(nums)):
                    nums[start], nums[i] = nums[i], nums[start]
                    backtrack(start + 1)
                    nums[start], nums[i] = nums[i], nums[start]

        permutations = []
        backtrack(0)
        return permutations

solution = Solution()
print(solution.permute([1,2,3]))