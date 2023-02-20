# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode):
        if not root:
            return []
        ans = []
        def pre(node):
            nonlocal ans
            if node:
                ans.append(node.val)
                pre(node.left)
                pre(node.right)
        pre(root)
        return ans
