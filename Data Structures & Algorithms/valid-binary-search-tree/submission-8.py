# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        list_of_roots = []
        is_valid = True
        
        def dfs(root: Optional[TreeNode]):
            nonlocal is_valid
            if root is None:
                return

            dfs(root.left)

            if len(list_of_roots) >= 1:
                if root.val <= list_of_roots[-1]:
                    is_valid = False
            list_of_roots.append(root.val)

            dfs(root.right)

        dfs(root)
        return is_valid
        