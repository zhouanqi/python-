class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def serialize(self, root):
        # write code here  
        def Pre_Order(root):
            if root:
                result.append(str(root.val))
                Pre_Order(root.left)
                Pre_Order(root.right)
            else:
                result.append("#")

        result = []
        Pre_Order(root)
        return ",".join(result)

    def deserialize(self, s):
        # write code here  
        s = s.split(",")

        def Change(num):
            num[0] += 1
            if num[0] < len(s):
                if s[num[0]] == '#':
                    return None
                root = TreeNode(int(s[num[0]]))
                root.left = Change(num)

                root.right = Change(num)
                return root
            else:
                return None
        num = [-1]
        return Change(num) 