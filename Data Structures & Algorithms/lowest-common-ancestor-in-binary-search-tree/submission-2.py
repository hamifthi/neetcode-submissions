# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.common_ancestor = None

        def dfs(root: TreeNode, p: TreeNode, q: TreeNode):
            if (p.val < root.val < q.val) or (q.val < root.val < p.val):
                self.common_ancestor = root
                return
            elif (root.val > q.val) and (root.val > p.val):
                dfs(root.left, p, q)
                return
            elif (root.val < q.val) and (root.val< p.val):
                dfs(root.right, p, q)
                return
            elif root.val == p.val:
                self.common_ancestor = p
                return
            elif root.val == q.val:
                self.common_ancestor = q
                return
        
        dfs(root, p, q)
        return self.common_ancestor