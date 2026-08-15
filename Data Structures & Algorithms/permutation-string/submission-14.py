from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter_1 = defaultdict(int)
        for char in s1:
            counter_1[char] += 1
        i = 0
        j = len(s1)
        while j <= len(s2):
            substring = s2[i:j]
            counter_2 = defaultdict(int)
            for char in substring:
                counter_2[char] += 1
            if counter_1 == counter_2:
                return True
            i += 1
            j += 1
        return False
        