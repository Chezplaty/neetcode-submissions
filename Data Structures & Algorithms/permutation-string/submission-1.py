class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        chars = [0] * 26
        chars2 = [0] * 26

        for c in s1:
            chars[ord(c) - ord('a')] += 1
        
        for c in s2[:len(s1)]:
            chars2[ord(c) - ord('a')] += 1
        
        l, r = 0, len(s1) - 1

        while r < len(s2):

            if chars == chars2:
                return True

            chars2[ord(s2[l]) - ord('a')] -= 1
            l += 1
            r += 1
            if r == len(s2):
                break
            
            chars2[ord(s2[r]) - ord('a')] += 1
        
        return False


