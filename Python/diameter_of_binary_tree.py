# Diameter of Binary Tree

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def diameterOfBinaryTree(self, root):
        def diameter(node, res):
            if not node:
                return 0
            
            left = diameter(node.left, res)
            right = diameter(node.right, res)

            res[0] = max(res[0], left + right)
            
            return max(left, right) + 1
        
        res = [0]
        diameter(root, res)
        return res[0]

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

test = Solution()
print(test.diameterOfBinaryTree(root))