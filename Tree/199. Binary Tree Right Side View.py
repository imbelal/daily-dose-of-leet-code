# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        lst = []
        lvl = []
        self.dfs(root, lst, lvl, 0)
        return lst

    def dfs(self, root: Optional[TreeNode], lst: List[int], lvl: List[int], c: int):
        if root == None:
            return
        if c not in lvl:
            lst.append(root.val)
            lvl.append(c)
        if root.right:
            self.dfs(root.right, lst, lvl, c+1)
        if root.left:
            self.dfs(root.left, lst, lvl, c+1)


1
2, 3
4
