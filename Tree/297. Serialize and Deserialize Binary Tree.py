# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        if not root:
            return "N"
        txt = str(root.val) + ";"
        queue = [root]
        while len(queue) > 0:
            curr = queue.pop(0)
            if curr.left:
                txt += str(curr.left.val) + ";"
                queue.append(curr.left)
            else:
                txt += str("N") + ";"
            if curr.right:
                txt += str(curr.right.val) + ";"
                queue.append(curr.right)
            else:
                txt += str("N") + ";"
        return txt[0: -1]

    def deserialize(self, data):
        if data == "N":
            return TreeNode()

        arr = data.split(";")
        root = TreeNode(int(arr[0]))

        queue = [root]
        i = 1
        c = 0

        while len(queue) > 0:
            curr = queue.pop(0)

            if arr[i] != "N":
                curr.left = TreeNode(arr[i])
                queue.append(curr.left)
                c += 1
            else:
                c -= 1
            i += 1

            if arr[i] != "N":
                curr.right = TreeNode(arr[i])
                queue.append(curr.right)
                c += 1
            else:
                c -= 1
            i += 1
        return root


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

ser = Codec()
deser = Codec()

print(ser.serialize(root))
ans = deser.deserialize(ser.serialize(root))


# 0 1 2 3 4 5 6 7 8 9 10
# 1;2;3;N;N;4;5;N;N;N;N

# c= 0
# 2 + i + c = L
# 2 + i + c + 1 = R
