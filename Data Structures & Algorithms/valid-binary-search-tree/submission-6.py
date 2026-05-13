# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return False
        
        def check_valid(node, left, right):

            if not node:
                return True
            
            if not (node.val > left and node.val < right):
                return False
            
            return check_valid(node.left, left, node.val) and check_valid(node.right, node.val, right)
        
        return check_valid(root, float('-inf'), float('inf'))
        