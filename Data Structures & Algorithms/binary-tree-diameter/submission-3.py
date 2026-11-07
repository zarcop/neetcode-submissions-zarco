# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.largest_path = 0


        def dfs(node):
            if not node:
                return 0 
            path = dfs(node.right) + dfs(node.left)
            self.largest_path = max(path, self.largest_path)
            
            return 1 + max(dfs(node.right), dfs(node.left))
        dfs(root)

        return self.largest_path
        

        