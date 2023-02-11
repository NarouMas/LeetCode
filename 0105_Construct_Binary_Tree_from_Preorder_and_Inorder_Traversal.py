# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder, inorder):
        rootIndex = 0
        while inorder[rootIndex] != preorder[0]:
            rootIndex += 1
        
        def foo(index, preIndex, l):
            node = TreeNode(l[index])
            # handle left subtree 
            if index != 0:
                leftTree = l[:index]
                i = 0
                while leftTree[i] != preorder[preIndex + 1]:
                    i += 1
                node.left = foo(i, preIndex + 1, leftTree)
            # handle right subtree
            if index != len(l) - 1:
                i = j = 0
                rightTree = l[index + 1:]
                # target is right subtree's root value
                if index == 0:
                    target = preorder[preIndex + 1]
                    preIndex += 1
                    j = preIndex
                else:
                    preIndex += index + 1
                    target = preorder[preIndex]
                while rightTree[i] != target:
                    i += 1
                node.right = foo(i, preIndex, rightTree)
            return node
        
        return foo(rootIndex, 0, inorder)
    def preOrder(self, node):
        print(node.val, end=', ')
        if node.left is not None:
            self.preOrder(node.left)
        if node.right is not None:
            self.preOrder(node.right)
    def inOrder(self, node):
        if node.left is not None:
            self.inOrder(node.left)
        print(node.val, end=', ')
        if node.right is not None:
            self.inOrder(node.right)


if __name__ == "__main__":
    a = Solution()
    root = a.buildTree([120, 140, 130, 125, 135],
                       [120, 125, 130, 135, 140])
    a.preOrder(root)
    print()
    a.inOrder(root)