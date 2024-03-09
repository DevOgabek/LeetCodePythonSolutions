# Combination Sum

class Solution(object):
    def combinationSum(self, candidates, target):
        def backtrack(start, target, path):
            if target == 0:
                result.append(path)
                return
            if target < 0:
                return
            for i in range(start, len(candidates)):
                backtrack(i, target - candidates[i], path + [candidates[i]])

        result = []
        candidates.sort()
        backtrack(0, target, [])
        return result

solution = Solution()
print(solution.combinationSum([2,3,6,7], 7))