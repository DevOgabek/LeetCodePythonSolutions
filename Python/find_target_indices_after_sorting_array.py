# Find Target Indices After Sorting Array

class Solution(object):
    def targetIndices(self, nums, target):
        lessThanCount = 0
        equalCount = 0
        
        for x in nums:
            if x == target:
                equalCount += 1
            elif x < target:
                lessThanCount += 1
                
        results = []
        
        l = lessThanCount
        r = l + equalCount
        for i in range(l, r):
            results.append(i)
            
        return results

solution = Solution()
print(solution.targetIndices([1,2,5,2,3], 2))