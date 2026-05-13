class Solution:
    def isPalindrome(self, s: str) -> bool:

        pointer1 = 0
        pointer2 = len(s) - 1

        while pointer1 < pointer2:
            if not s[pointer1].isalnum():
                pointer1 += 1
                continue

            if not s[pointer2].isalnum():
                pointer2 -= 1
                continue

            if s[pointer1].lower() != s[pointer2].lower():
                return False

            pointer1 += 1
            pointer2 -= 1

        return True
