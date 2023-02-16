class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = []
        for i in range(len(s)):
            if s[i].isalnum():
                new.append(s[i].lower())
        l = 0
        r = len(new) - 1
        while l <= r:
            if new[l] != new[r]:
                return False
            l += 1
            r -= 1
            
        return True