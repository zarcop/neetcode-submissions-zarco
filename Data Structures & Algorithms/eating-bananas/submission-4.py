import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        """
        h = number of hours you have to eat all bananas
        you have to eat your ananes per hou eating rate of k

        """

        max_pile = float("-inf")

        for pile in piles:
            max_pile = max(pile, max_pile)

        left = 1
        right = max_pile

        min_speed = max_pile

        while left <= right:
            m_speed = (right + left) // 2
            current_h = 0
            for i in range(len(piles)):
                 pile = piles[i]
                 hours =  -(pile // -m_speed)
                 current_h += hours
            if current_h  > h :
                left = m_speed + 1
            elif current_h <= h:
                min_speed = min(min_speed, m_speed)
                right = m_speed - 1
        return min_speed
    
            


                 
            

                
                





        







        