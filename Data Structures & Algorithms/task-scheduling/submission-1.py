import heapq

from collections import defaultdict

from collections import deque


class Solution:


    '''
    cpu tasks

    where task[i] is a ltter beween A and Z
    you are given integer 
    '''
    def leastInterval(self, tasks: List[str], n: int) -> int:

        

        freq_table = defaultdict(int)


        for task in tasks:
            freq_table[task] += 1
        
        heap = [-freq for freq in freq_table.values()]
        heapq.heapify(heap)

        time = 0
        queue = deque()

        while heap or queue:
            time += 1
            if heap:
                count = heapq.heappop(heap) + 1
                if count != 0:
                    queue.append((count, time + n))
            if queue and queue[0][1] == time:
                heapq.heappush(heap, queue.popleft()[0])
        
        return time
        
            
        





    
        


        
            
        
            



        


        