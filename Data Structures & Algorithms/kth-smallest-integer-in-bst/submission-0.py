# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nums = []

        def add_nums(node):
            if not node:
                return
            
            add_nums(node.left)
            nums.append(node.val)
            add_nums(node.right)
        
        add_nums(root)
        return nums[k-1]

        

            