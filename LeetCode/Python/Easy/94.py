#Binary Tree InOrder Traversal
# Definition for a binary tree node.
import sys


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode):

        # if root:
        pass
        print(root.val)
            # First recur on left child
            # self.inorderTraversal(self.left)

            # then print the data of node
            # sys.stdout.write(root.val)

            # now recur on right child
            # self.inorderTraversal(root.right)


x = Solution()
print(x.inorderTraversal([1,0,2,3]))