# Binary Subarrays With Sumvv

class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        count = {0: 1}
        curr_sum = 0
        total_subarrays = 0
        
        for num in nums:
            curr_sum += num
            if curr_sum - goal in count:
                total_subarrays += count[curr_sum - goal]
            count[curr_sum] = count.get(curr_sum, 0) + 1

        return total_subarrays
    
solution = Solution()
print(solution.numSubarraysWithSum([1,0,1,0,1], 2))