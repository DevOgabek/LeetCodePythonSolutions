# Decompress Run-Length Encoded List

class Solution(object):
    def decompressRLElist(self, nums):
        arr = []
        for i in range(0, len(nums), 2):
            arr += [nums[i+1]] * nums[i]
        return arr

test = Solution()
print(test.decompressRLElist([1,2,3,4]))