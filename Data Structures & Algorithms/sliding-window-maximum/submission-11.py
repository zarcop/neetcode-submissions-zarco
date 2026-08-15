import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxheap = []
        result = []
        left = 0

        for i in range(k):
            heapq.heappush(maxheap, [-nums[i], i])
        result.append( - maxheap[0][0])
        left = 1
        for right in range(k, len(nums)):
            heapq.heappush(maxheap, [-nums[right], right])
            while maxheap[0][1] < left:
                heapq.heappop(maxheap)
            max_window = -maxheap[0][0]
            result.append(max_window)
            left += 1
        return result



        
        







        



        
        
        

        




    


        

        



        