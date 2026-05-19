class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        if s == t:
            return s

        count_t = {}

        for char in t:
            count_t[char] = 1 + count_t.get(char, 0)
        
        count_s = {}

        have, need = 0, len(count_t)
        res = ''
        res_len = float('inf')
        l, r = 0, 0
        while r < len(s):
            char = s[r]
            count_s[char] = 1 + count_s.get(char, 0)

            if char in count_t and count_s[char] == count_t[char]:
                have += 1
            
            while have == need:
                # update result BEFORE shrinking
                if (r - l + 1) < res_len:
                    res_len = r - l + 1
                    res = s[l:r + 1]

                count_s[s[l]] -= 1

                if s[l] in count_t and count_s[s[l]] < count_t[s[l]]:
                    have -= 1

                l += 1
            
            r += 1
    
        return res

        