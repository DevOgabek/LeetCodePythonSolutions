# Subsets

class Solution(object):
    def subsets(self, nums):
        def backtrack(start, curr_subset):
            result.append(curr_subset[:])
            
            for i in range(start, len(nums)):
                curr_subset.append(nums[i])
                backtrack(i + 1, curr_subset)
                curr_subset.pop()

        result = []
        backtrack(0, [])
        return result

solution = Solution()
print(solution.subsets([1,2,3]))