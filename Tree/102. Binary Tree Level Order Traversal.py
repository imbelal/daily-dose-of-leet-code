# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if root is None:
            return res
        queue = [root]
        res.append([root.val])
        level = 1
        newArr = []
        counter = 0
        while len(queue) > 0:
            cur_node = queue.pop(0)
            level -= 1
            if cur_node.left is not None:
                queue.append(cur_node.left)
                newArr.append(cur_node.left.val)
                counter += 1

            if cur_node.right is not None:
                queue.append(cur_node.right)
                newArr.append(cur_node.right.val)
                counter += 1
            if len(newArr) > 0 and level == 0:
                res.append(newArr)
                newArr = []
                level = counter
                counter = 0
        return res

  
