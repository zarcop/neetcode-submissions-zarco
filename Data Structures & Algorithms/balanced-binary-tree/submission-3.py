# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        def depth(node):
            if node == None:
                return 0
            left = depth(node.left)
            right = depth(node.right)
            max_depth =  1 + max(left, right)
            return max_depth
        left_depth = depth(root.left)
        right_depth = depth(root.right)
        difference = abs(left_depth - right_depth)
        if difference > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
        
        