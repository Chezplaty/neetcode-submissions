class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        l = 0

        max_length = 0

        for r in range(len(s)):
            #s[r] is the current character in the substring
            counts[s[r]] = 1 + counts.get(s[r], 0)

            max_replace = max(counts.values())
            
            window = r - l + 1
            #remove the count of the letter at l from the dictionary
            if window - max_replace> k:
                counts[s[l]] -= 1
                l += 1
                window -= 1


            if window > max_length:
                max_length = window
        
        return max_length






            

