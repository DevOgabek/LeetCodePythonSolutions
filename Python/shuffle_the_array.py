# Shuffle the Array

class Solution(object):
    def shuffle(self, nums, n):
        result = []
        for i in range(n):
            result.extend([nums[i], nums[i + n]])
        return result

test = Solution()
print(test.shuffle([2,5,1,3,4,7], 3))