# Same Tree

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p, q):
        stack = [(p, q)]
        while stack:
            node1, node2 = stack.pop()
            if not node1 and not node2:
                continue
            if not node1 or not node2 or node1.val != node2.val:
                return False
            stack.append((node1.left, node2.left))
            stack.append((node1.right, node2.right))
        return True

tree1 = TreeNode(1, TreeNode(2), TreeNode(3))
tree2 = TreeNode(1, TreeNode(2), TreeNode(3))

test = Solution()
print(test.isSameTree(tree1, tree2))