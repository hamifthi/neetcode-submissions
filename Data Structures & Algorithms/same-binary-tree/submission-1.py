# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.identical = True

        def dfs(p: Optional[TreeNode], q: Optional[TreeNode]) -> None:
            if p is None and q is None:
                return
            elif p is None or q is None:
                self.identical = False
                return
            elif p and q:
                if p.val != q.val:
                    self.identical = False
                    return

            dfs(p.left, q.left)
            dfs(p.right, q.right)
            return
        
        dfs(p, q)
        return self.identical