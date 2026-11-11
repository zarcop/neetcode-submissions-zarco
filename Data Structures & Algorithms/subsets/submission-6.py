class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        result = []

        def iterate(start_i, current_path):
            result.append(list(current_path))
            for i in range(start_i, len(nums)):

                current_path.append(nums[i])

                iterate(i + 1, current_path)
                current_path.pop()
        iterate(0, [])

        return result
            
            
            

        