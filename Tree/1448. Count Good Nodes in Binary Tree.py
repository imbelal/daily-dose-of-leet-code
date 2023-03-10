# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        count = 0
        count = self.dfs(root, root.val, count)
        return count

    def dfs(self, root: TreeNode, max: int, count: int):
        if not root:
            return count
        elif root.val >= max:
            max = root.val
            count += 1
        count = self.dfs(root.left, max, count)
        count = self.dfs(root.right, max, count)
        return count


s = Solution()
root = TreeNode(3)
root.left = TreeNode(1)
root.left.left = TreeNode(3)
root.right = TreeNode(4)
root.right.left = TreeNode(1)
root.right.right = TreeNode(5)


print(s.goodNodes(root))
