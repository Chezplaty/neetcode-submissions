class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        total = sum(nums)
        target = total / 2

        dp = set()
        dp.add(0)
        for i in range(len(nums) -1, -1, -1):
            for n in list(dp):
                sum_num = nums[i] + n
                if sum_num == target:
                    return True
                
                if sum_num < target:
                    dp.add(sum_num)
        
        print(dp)
        return False


