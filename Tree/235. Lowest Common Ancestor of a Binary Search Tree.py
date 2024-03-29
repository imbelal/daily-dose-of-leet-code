# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return root
        elif root.val >= p.val and root.val <= q.val:
            return root
        elif root.val >= q.val and root.val <= p.val:
            return root
        else:
            return self.lowestCommonAncestor(root.left, p, q) or self.lowestCommonAncestor(root.right, p, q)
            
