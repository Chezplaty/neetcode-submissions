class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numSet = set(nums)

        longest = 0

        for num in nums:
            #check if its the start of a sequence
            if (num - 1) not in numSet:
                length = 0
                while (num + length) in numSet:
                    length += 1
                
                if length > longest:
                    longest = length
        
        return longest
            


        


        