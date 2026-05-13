class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        length = len(nums)
        res = []

        count = {}
        
        max_num = nums[0]

        for i in range(k):
            num = nums[i]
            count[num] = count.get(num, 0) + 1
            if num > max_num:
                max_num = num
        
        res.append(max_num)
        

        if length == k:
            return res

        left = 0
        for r in range(k, length):
            left_num = nums[left]
            count[left_num] -= 1
            count[nums[r]] = count.get(nums[r],0) + 1

            if count[left_num] == 0:
                count.pop(left_num)

            max_num = nums[r]
            for num in count:
                if num > max_num:
                    max_num = num
            res.append(max_num)
            left += 1
        
        return res




