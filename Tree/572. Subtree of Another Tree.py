# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root and subRoot:
            if(self.isSameTree(root, subRoot)):
                return True
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p and q:
            if p.val == q.val:
                return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
            else:
                return False
        elif p != q:
            return False
        else:
            return True


s = Solution()
root = TreeNode(1)
root.left = TreeNode(1)
# root.left.left = TreeNode(1)
# root.left.right = TreeNode(2)
# root.right = TreeNode(5)

root2 = TreeNode(1)
# root2.left = TreeNode(1)
# root2.right = TreeNode(2)

print(s.isSubtree(root, root2))
