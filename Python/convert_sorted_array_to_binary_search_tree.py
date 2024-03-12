# Convert Sorted Array to Binary Search Tree

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def sortedArrayToBST(self, nums):
        def helper(start, end):
            if start > end:
                return None
            mid = (start + end) // 2
            root = TreeNode(nums[mid])
            root.left = helper(start, mid - 1)
            root.right = helper(mid + 1, end)
            return root

        return helper(0, len(nums) - 1)
    
solution = Solution()
print(solution.sortedArrayToBST([1,2,3,4]))