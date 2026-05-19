class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0

        counts = {}

        max_length = 0
        max_freq = 0

        for r in range(len(s)):
            counts[s[r]] = 1 + counts.get(s[r], 0)

            max_freq = max(max_freq, counts[s[r]])

            window = r - l + 1
            if window - max_freq > k:
                counts[s[l]] -= 1;
                l += 1
                window -= 1
            
            max_length = max(max_length, window)
        
        return max_length