#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

class Solution:
    def maxDepth(self, root) -> int:
        if not root:
            return 0
        q = deque()
        q.append((1, root))
        ans = 0
        while q:
            level, node = q.popleft()
            ans = max(ans, level)
            if node.left is not None:
                q.append((level + 1 , node.left))
            if node.right is not None:
                q.append((level + 1, node.right))
        return ans

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
    print(a.maxDepth(node1))