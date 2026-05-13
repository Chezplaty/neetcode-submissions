# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 0

        n = 0
        stack = []
        cur = root


        while cur or stack:
            if not cur:
                if not stack:
                    return 0

                cur = stack.pop()
                n += 1
                if n == k:
                    return cur.val
                cur = cur.right
            else:
                stack.append(cur)
                cur = cur.left
            
            

        

            