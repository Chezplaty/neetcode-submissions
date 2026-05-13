class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1 = len(s1)
        len2 = len(s2)
        
        if len1 > len2:
            return False
        
        char1 = {}
        char2 = {}

        for i in range(len1):
            char1[s1[i]] = 1 + char1.get(s1[i], 0)
            char2[s2[i]] = 1 + char2.get(s2[i], 0)
        
        if char1 == char2:
            return True

        
        i = len1
        left = 0
        while i < len2:
            char2[s2[i]] = 1 + char2.get(s2[i], 0)
            char2[s2[left]] -= 1
            if char2[s2[left]] == 0:
                del char2[s2[left]]
            
            if char1 == char2:
                return True
            
            i += 1
            left += 1

        return False

