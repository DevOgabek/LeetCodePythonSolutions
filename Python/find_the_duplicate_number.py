# Find the Duplicate Number

class Solution(object):
    def findDuplicates(self, nums):
        p = 10 ** 5 + 3
        ans = []
        
        for x in nums:
            next = (x % p) - 1
            if nums[next] > p:
                ans.append(next + 1)
            nums[next] += p
            
        return ans
    
solution = Solution()
print(solution.findDuplicates([4,3,2,7,8,2,3,1]))