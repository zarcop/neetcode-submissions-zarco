class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = {}

        def recursion(n_step: int) -> int:
            if n_step >= len(cost):
                return 0
            if n_step in cache:
                return cache[n_step]

            # Cost of standing on this step + cheapest path from here to the top
            cache[n_step] = cost[n_step] + min(
                recursion(n_step + 1),
                recursion(n_step + 2)
            )
            return cache[n_step]

        return min(recursion(0), recursion(1))
        
        