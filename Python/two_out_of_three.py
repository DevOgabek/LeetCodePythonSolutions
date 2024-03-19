# Two Out of Three

class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        nums = set(nums1 + nums2 + nums3)
        arr = []
        for num in nums:
            count = 0
            if num in nums1:
                count += 1
            if num in nums2:
                count += 1
            if num in nums3:
                count += 1
            if count > 1:
                arr.append(num)
                
        return arr
    
solution = Solution()
print(solution.twoOutOfThree([1,1,3,2], [2,3], [3]))