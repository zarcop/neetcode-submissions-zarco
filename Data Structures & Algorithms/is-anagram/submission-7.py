class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counterS = {}
        counterT = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            char = s[i]
            counterS[char] = 1 + counterS.setdefault(char, 0)
        for i in range(len(t)):
            char = t[i]
            counterT[char] =  1 + counterT.setdefault(char, 0)
        
        if counterS == counterT:
            return True
        else:
            return False


        