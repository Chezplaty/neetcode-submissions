# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        q = collections.deque()
        q.append(root)

        while q:
            qLen = len(q)
            level = []
            for i in range(qLen):
                new_root = q.popleft()
                if new_root:
                    level.append(new_root.val)
                    q.append(new_root.left)
                    q.append(new_root.right)
            if level:
                res.append(level)
        
        return res

            

        

        