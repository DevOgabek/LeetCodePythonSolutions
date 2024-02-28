# Find Bottom Left Tree Value

from collections import deque

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

class Solution(object):
    def findBottomLeftValue(self, root):
        queue = deque([root])
        leftmost_value = None

        while queue:
            node = queue.popleft()

            leftmost_value = node.val

            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)

        return leftmost_value

root = TreeNode(2, TreeNode(1), TreeNode(3))

test = Solution()
print(test.findBottomLeftValue(root))