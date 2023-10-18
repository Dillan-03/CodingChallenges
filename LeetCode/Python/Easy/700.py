# 700 Search in a Binary tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if (root == null):
            return null
        if (root.val == val):
            return root

        if (val < root.val):
            searchBST(root.left, val)
        else:
            searchBST(root.right, val)
