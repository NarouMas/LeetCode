# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque

class Solution:
    def levelOrder(self, root):
        if root is None:
            return []
        q = deque([root])
        ans = [[]]
        level = 0
        remainNode = 1
        currentLevelNode = 0

        while q:
            node = q.popleft()
            ans[level].append(node.val)

            if node.left is not None:
                q.append(node.left)
                currentLevelNode += 1
            if node.right is not None:
                q.append(node.right)
                currentLevelNode += 1

            remainNode -= 1
            if remainNode == 0 and q:
                level += 1
                remainNode = currentLevelNode
                currentLevelNode = 0
                ans.append([])
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
    print(a.levelOrder(node1))