class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        check1 = {}
        check2 = {}
        
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] in check1.keys():
                check1[s[i]] += 1
            else: 
                check1[s[i]] = 0
            if t[i] in check2.keys():
                check2[t[i]] += 1
            else: 
                check2[t[i]] = 0
        if check1 == check2:
            return True
        else: 
            return False
        