class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = collections.deque()
        l = 0

        for r in range(len(nums)):
            
            while q and nums[r] > nums[q[-1]]: #element at the end of the deque
                q.pop()

            q.append(r)

            if r - l + 1 == k:
                res.append(nums[q[0]]) #append the first element in the deque
                
                if l == q[0]:
                    q.popleft()
                l += 1
            
        return res
            
