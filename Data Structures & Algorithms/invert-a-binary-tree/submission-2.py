# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        #recursing 
        if not root:
            return root

        if root.left:
            self.invertTree(root.left)
        
        if root.right:
            self.invertTree(root.right)

        r_holder = root.right if root.right else None
        l_holder = root.left if root.left else None
        root.left = r_holder
        root.right = l_holder

        return root

        