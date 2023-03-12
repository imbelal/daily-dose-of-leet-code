# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(root, k: int, stk: list) -> int:
            if not root:
                k -= 1
                x = stk.pop()
                if k == 0:
                    return x.val
                else:
                    return dfs(x.right, k, stk)
            stk.append(root)
            return dfs(root.left, k, stk)
        return dfs(root, k, [])


s = Solution()
root = TreeNode(5)
root.left = TreeNode(3)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.left.left.left = TreeNode(1)
root.right = TreeNode(6)


print(s.kthSmallest(root, 3))
