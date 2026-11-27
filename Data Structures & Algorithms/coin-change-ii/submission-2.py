class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = {}

        def sum_money(curr_sum: int, index: int) -> int:
            if curr_sum == amount:
                return 1
            if curr_sum > amount or index >= len(coins):
                return 0
            if (curr_sum, index) in cache:
                return cache[(curr_sum, index)]

            cache[(curr_sum, index)] = (
                sum_money(curr_sum + coins[index], index)
                + sum_money(curr_sum, index + 1)
            )
            return cache[(curr_sum, index)]

        return sum_money(0, 0)

        


        return sum_money(0, 0)
            
        