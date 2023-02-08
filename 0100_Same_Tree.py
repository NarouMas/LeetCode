# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p, q) -> bool:
        if p is None and q is None:
            return True
        if (p is None) ^ (q is None):
            return False
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

if __name__ == "__main__":
    a = Solution()
    # node6 = TreeNode(3, None, None)
    # node7 = TreeNode(7, None, None)
    # node2 = TreeNode(4, None, None)
    # node3 = TreeNode(6, node6, node7)
    # node1 = TreeNode(5, node2, node3)
    node12 = TreeNode(125, None, None)
    node13 = TreeNode(145, None, None)
    node6 = TreeNode(130, node12, node13)
    node3 = TreeNode(140, node6, None)
    node1 = TreeNode(120, None, node3)
    print(a.isSameTree(node1, node3))