class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ''

        char_s = {}
        char_t = {}
        for char in t:
            char_t[char] = 1 + char_t.get(char,0)


        l = 0

        #duplicates should not be counted so len(char_t)
        have, need = 0, len(char_t)
        res = ''
        res_len = float('inf')
        for r in range(len(s)):
            char = s[r]
            char_s[char] = 1 + char_s.get(char, 0)
            
            if char in char_t and char_s[char] == char_t[char]:
                have += 1
            
            while have == need:
                char_left = s[l]

                if r - l + 1 < res_len:
                    res = s[l : r + 1]
                    res_len = r - l + 1

                char_s[char_left] -= 1
                if char_left in char_t and char_s[char_left] < char_t[char_left]:
                    have -= 1
                l += 1
                    
        
        return res
            
                



            
