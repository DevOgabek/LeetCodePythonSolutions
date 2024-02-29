# Even Odd Tree

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isEvenOddTree(self, root):
        if not root:
            return True

        queue = deque([root])
        level = 0

        while queue:
            prev_val = None

            for _ in range(len(queue)):
                node = queue.popleft()

                if (level % 2 == 0 and (node.val % 2 == 0 or (prev_val is not None and node.val <= prev_val))) or \
                   (level % 2 == 1 and (node.val % 2 == 1 or (prev_val is not None and node.val >= prev_val))):
                    return False

                prev_val = node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            level += 1

        return True

root = TreeNode(1)
root.left = TreeNode(10)
root.right = TreeNode(4)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.right = TreeNode(9)

solution = Solution()
print(solution.isEvenOddTree(root))
