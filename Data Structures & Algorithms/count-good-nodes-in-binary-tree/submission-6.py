# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def goodMax(node, max_val):
            if node is None:
                return 0
            if node.val >= max_val:
                return 1 + goodMax(node.right, node.val) + goodMax(node.left, node.val)
            else:
                return goodMax(node.right, max_val) + goodMax(node.left, max_val)

        return goodMax(root, root.val)
                
        
        

        