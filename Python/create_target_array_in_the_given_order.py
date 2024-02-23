# Create Target Array in the Given Order

class Solution(object):
    def createTargetArray(self, nums, index):
        arr = []
        for i, num in zip(index, nums):
            arr.insert(i, num)
        return arr

test = Solution()
print(test.createTargetArray([0,1,2,3,4], [0,1,2,2,1]))