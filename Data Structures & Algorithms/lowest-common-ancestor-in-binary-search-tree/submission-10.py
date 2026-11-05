# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def findpath(node, target, tranversal_list):
            if not node:
                return None
            tranversal_list.append(node)
            if target.val == node.val:
                return tranversal_list
            if target.val < node.val:
                return findpath(node.left, target, tranversal_list)
            if target.val > node.val:
                return findpath(node.right, target, tranversal_list)
        path_p = findpath(root, p, [])
        path_q = findpath(root, q, [])
        lca = root
        for node_p, node_q in zip(path_p, path_q):
            if node_p == node_q:
                lca = node_p
            else:
                break
        return lca
            

        