import heapq


class MedianFinder:
    def __init__(self):
        self.left_heap = []   # max-heap (negated values) for the lower half
        self.right_heap = []  # min-heap (positive values) for the upper half

    def addNum(self, num: int) -> None:
        heapq.heappush(self.left_heap, -num)

        heapq.heappush(self.right_heap, -heapq.heappop(self.left_heap))
        if len(self.right_heap) > len(self.left_heap):
            heapq.heappush(self.left_heap, -heapq.heappop(self.right_heap))

    def findMedian(self) -> float:
        if len(self.left_heap) == len(self.right_heap):
            return (-self.left_heap[0] + self.right_heap[0]) / 2
        return float(-self.left_heap[0])
            
        
        