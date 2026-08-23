class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        '''
        largest histogram
        [i] * min length
        '''


        left_stack = []
        right_stack = []

        largest = float("-inf")
        pairs = {}

        for i in range(len(heights)):
            while left_stack and heights[left_stack[-1]] >= heights[i]:
                left_stack.pop()
            if left_stack:
                pairs[i] = [left_stack[-1]]
            else:
                pairs[i] = [-1]
            left_stack.append(i)


                
        for i in range(len(heights) - 1, -1 , -1):
            while right_stack and heights[right_stack[-1]] >= heights[i]:
                right_stack.pop()
            if right_stack:
                pairs[i].append(right_stack[-1])
            else:
                pairs[i].append(len(heights))
            right_stack.append(i)

        for i in range(len(heights)):
            left, right = pairs[i]
            area = heights[i] * (right - left - 1)
            largest = max(area, largest)

        return largest
            
            

            
                





        