class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        '''
        target_integer
        the same number can be chosen
        the combinations have to different
        '''
        result = []

        def backtrack(start_index, combination, rem_target):
            if rem_target < 0:
                return
            if rem_target == 0:
                result.append(combination.copy())
                return
            for i in range(start_index, len(nums)):
                combination.append(nums[i])
                backtrack(i, combination, rem_target - nums[i])

                combination.pop()

        backtrack(0, [], target)

        return result
                

            




    



        