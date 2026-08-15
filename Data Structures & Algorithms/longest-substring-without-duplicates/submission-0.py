class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        mappy = {}
        maxNum = 0
        left = 0
        for i in range(length):
            charSet = set()
            for j in range(i, length):
                if s[j] in charSet:
                    break
                charSet.add(s[j])
            maxNum = max(maxNum, len(charSet))
        return maxNum
            

          



            


        