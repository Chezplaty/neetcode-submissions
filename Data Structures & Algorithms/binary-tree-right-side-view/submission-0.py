# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = collections.deque()
        q.append(root)

        while q:
            qLen = len(q)
            not_popped = True
            for i in range(qLen):
                if not_popped:
                    new_root = q.popleft()
                    if new_root:
                        res.append(new_root.val)
                        q.append(new_root.right)
                        q.append(new_root.left)
                        not_popped = False
                else:
                    new_root = q.popleft()
                    if new_root:
                        q.append(new_root.right)
                        q.append(new_root.left)
        
        return res
            

