# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def dfs(node, traversal_list):
            if not node:
                traversal_list.append(None)
                return
            traversal_list.append(node.val)
            left = dfs(node.left, traversal_list)
            right = dfs(node.right, traversal_list)
        p_list = []
        q_list = []
        dfs(p, p_list)
        dfs(q, q_list)

        return p_list == q_list

        