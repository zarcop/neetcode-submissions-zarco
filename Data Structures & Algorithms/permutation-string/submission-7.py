from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        counter_1 = Counter(s1)
        i = 0
        j = len(s1)
        while j < len(s2) + 1:
            substring = s2[i:j]
            counter_2 = Counter(substring)
            if counter_1 == counter_2:
                return True
            i += 1
            j += 1
        return False

        

            


            

        