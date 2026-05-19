class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        count_1 = [0] * 26
        count_2 = [0] * 26

        for i in range(len(s1)):
            count_1[ord(s1[i]) - ord('a')] += 1
            count_2[ord(s2[i]) - ord('a')] += 1
        
        if count_1 == count_2:
            return True

        l, r = 0, len(s1)
        while r < len(s2):
            count_2[ord(s2[r]) - ord('a')] += 1
            count_2[ord(s2[l]) - ord('a')] -= 1
            if count_1 == count_2:
                return True
            
            l += 1
            r += 1
        
        return False