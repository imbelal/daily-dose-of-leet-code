# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def valid(node, left, right):
            if not node:
                return True
            if not (node.val < right and node.val > left):
                return False

            return valid(node.left, left, node.val) and valid(node.right, node.val, right)

        return valid(root, float("-inf"), float("inf"))


s = Solution()
root = TreeNode(32)
root.left = TreeNode(26)
root.left.left = TreeNode(19)
root.left.left.right = TreeNode(27)
root.right = TreeNode(47)
root.right.right = TreeNode(56)


print(s.isValidBST(root))
