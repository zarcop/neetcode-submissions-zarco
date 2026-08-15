class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        maxsub = 1
        left = 0
        right = 1
        while left < len(s) - 1:
            letter_set = set()
            letter_set.add(s[left])
            while right < len(s) and s[right] not in letter_set:
                letter_set.add(s[right])
                maxsub = max(len(letter_set), maxsub)
                right += 1
            left += 1
            right = left + 1
        return maxsub
                

        