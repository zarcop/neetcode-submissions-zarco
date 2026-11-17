class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        result = []
        def backtrack(curr_combination):
            if len(curr_combination) == len(nums):
                result.append(curr_combination.copy())
                return
            for num in nums:
                if num not in curr_combination:
                    curr_combination.append(num)
                    backtrack(curr_combination)
                    curr_combination.pop()
        backtrack([])
        return result




                


            

            

                

        



            

        