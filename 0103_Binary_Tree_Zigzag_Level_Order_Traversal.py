# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque

class Solution:
    def zigzagLevelOrder(self, root):
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
            if remainNode == 0:
                if level % 2 == 1:
                    ans[level] = ans[level][::-1]
                if q:
                    level += 1
                    remainNode = currentLevelNode
                    currentLevelNode = 0
                    ans.append([])
        return ans


if __name__ == "__main__":
    a = Solution()
    node7 = TreeNode(7, None, None)
    node6 = TreeNode(15, None, None)
    node3 = TreeNode(20, node6, node7)
    node2 = TreeNode(9, None, None)
    node1 = TreeNode(3, node2, node3)
    print(a.zigzagLevelOrder(node1))