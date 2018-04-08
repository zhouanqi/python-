
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: param root: The root of the binary search tree
    @param k1: An integer
    @param k2: An integer
    @return: return: Return all keys that k1<=key<=k2 in ascending order
    """
    def searchRange(self, root, k1, k2):
        # write your code her
        k1k2=[]
        def tree(root):
            if root.val==None:
                return k1k2
            if k1<=root.val<=k2:
                k1k2.append(root.val)
            if root.left!=None:
                tree(root.left)
            if root.right!=None:
                tree(root.right)
        if root!=None:        
            tree(root)
        k1k2.sort()
        return k1k2