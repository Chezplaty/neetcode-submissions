
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        frequency = [[] for i in range(len(nums) + 1)]
        res = []

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        for num, c in count.items():
            frequency[c].append(num)
        
        for i in range(len(frequency) - 1, -1, -1):
            for j in frequency[i]:
                res.append(j)
                k -= 1
                if k == 0:
                    return res



        
