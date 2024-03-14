# Next Greater Element I

class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        next_greater = {}

        for num in reversed(nums2):
            while stack and stack[-1] <= num:
                stack.pop()

            if stack:
                next_greater[num] = stack[-1]
            else:
                next_greater[num] = -1

            stack.append(num)

        ans = [next_greater[num] for num in nums1]
        return ans
    
solution = Solution()
print(solution.nextGreaterElement([4,1,2], [1,3,4,2]))