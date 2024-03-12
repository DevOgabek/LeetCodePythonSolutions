# Binary Tree Inorder Traversal

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def inorderTraversal(self, root):
        def traverse(node, result):
            if node is None:
                return
            traverse(node.left, result)
            result.append(node.val)
            traverse(node.right, result)

        result = []
        traverse(root, result)
        return result

root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

solution = Solution()

print(solution.inorderTraversal(root))