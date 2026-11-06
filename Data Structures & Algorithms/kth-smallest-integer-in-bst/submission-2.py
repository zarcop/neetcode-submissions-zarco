# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return []


        def dfs(node, traversal):
            if not node:
                return None
            dfs(node.left, traversal)

            traversal.append(node.val)

            dfs(node.right, traversal)
        sorted_traversal = []
        dfs(root, sorted_traversal)
        kth_smallest = sorted_traversal[k - 1] 
        return kth_smallest
        


    
        