# Contains Duplicate II

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        hashmap = {}
        for i in range(len(nums)):
            if nums[i] in hashmap:
                if abs(hashmap[nums[i]] - i) <= k:
                    return True
            hashmap[nums[i]] = i
        return False
    
solution = Solution()
print(solution.containsNearbyDuplicate([1,2,3,1], 3))