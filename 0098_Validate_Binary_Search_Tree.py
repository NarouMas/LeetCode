# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from functools import cache
class Solution:
    def isValidBST(self, root) -> bool:
        @cache
        def checkTreeV1(node, parentVal, grandVal, direction):
            if node is None:
                return True
            if node.left is not None and node.left.val >= node.val:
                return False
            if node.right is not None and node.right.val <= node.val:
                return False
            
            if direction % 10 == 1:
                if node.right is not None and node.right.val >= parentVal:
                    return False
            elif direction % 10 == 2:
                if node.left is not None and node.left.val <= parentVal:
                    return False
            
            if direction == 12: #LR
                if node.right is not None and node.right.val >= grandVal:
                    return False
            elif direction == 21: #RL
                if node.left is not None and node.left.val <= grandVal:
                    return False
            
            direction = (direction % 10) * 10
            return checkTreeV1(node.left, node.val, parentVal, direction + 1) and checkTreeV1(node.right, node.val, parentVal, direction + 2)

        @cache
        def checkTree(node, little, large):
            if node is None:
                return True
            if node.val <= little or node.val >= large:
                return False
            return checkTree(node.left, little, node.val) and checkTree(node.right, node.val, large)
            

        return checkTree(root, float('-inf'), float('inf'))
        #direction 
        # 0: root
        # 1: L
        # 2: R
        # 11: LL
        # 22: RR
        # 12: LR
        # 21: RL

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
    print(a.isValidBST(node1))