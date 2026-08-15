# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(Node):
            if Node is  not None:
                Noderight = Node.right
                Node.right = Node.left
                Node.left = Noderight
                dfs(Node.left)
                dfs(Node.right)
            else:
                return
        dfs(root)
        return root
        