#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.ans = root.val
        def gain_from_subtree(node):
            if not node:
                return 0
            left_gain = max(gain_from_subtree(node.left), 0)
            right_gain = max(gain_from_subtree(node.right), 0)
            self.ans = max(left_gain + right_gain + node.val, self.ans)
            return max(left_gain, right_gain) + node.val
        gain_from_subtree(root)
        return self.ans
if __name__ == "__main__":
    a = Solution()
    node7 = TreeNode(-2, None, None)
    node6 = TreeNode(-7, None, None)
    node3 = TreeNode(-5, node6, node7)
    node2 = TreeNode(-3, None, None)
    node1 = TreeNode(-10, node2, node3)
    print(a.maxPathSum(node1))