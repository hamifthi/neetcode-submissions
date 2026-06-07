# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        if root.val and root.left is None and root.right is None:
            return 1

        max_left = self.maxDepth(root.left)
        max_right = self.maxDepth(root.right)
        return 1 + max(max_left, max_right)
