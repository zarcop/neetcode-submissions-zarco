class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def backtrack(start_index,combination, remaining):
            if remaining < 0:
                return
            
            if remaining == 0:
                result.append(combination.copy())
                return
            
            for i in range(start_index, len(candidates)):
                if i > start_index and candidates[i] == candidates[i - 1]:
                    continue
                
                combination.append(candidates[i])

                backtrack(i + 1, combination, remaining - candidates[i])

                combination.pop()
    
        backtrack(0, [], target)
        return result

        

    


    
        