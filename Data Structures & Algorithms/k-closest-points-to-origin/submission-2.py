import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        heap_distances = [] # min heap
        k_points =[]

        for i in range(len(points)):
            x, y = points[i]
            distance = math.sqrt((abs(x) ** 2 ) + (abs(y) ** 2)) 
            tup = (distance, i)
            heapq.heappush(heap_distances, tup)
        

        for _ in range(k):
            distance, i = heapq.heappop(heap_distances)
            k_point = points[i]
            k_points.append(k_point)
        return k_points

        








        