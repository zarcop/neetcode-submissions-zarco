class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}

        def recursion(n_step: int) -> int:
            if n_step == n:
                return 1  
            if n_step > n:
                return 0  
            if n_step in cache:
                return cache[n_step]

            cache[n_step] = recursion(n_step + 1) + recursion(n_step + 2)
            return cache[n_step]

        return recursion(0)
            

            





        