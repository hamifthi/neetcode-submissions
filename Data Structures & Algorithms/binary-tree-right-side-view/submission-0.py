# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        queue = deque([root])
        result = []

        while queue:
            current_level = len(queue)
            current_nodes = []

            for i in range(current_level):
                node = queue.popleft()
                current_nodes.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(current_nodes[-1])
        
        return result
        