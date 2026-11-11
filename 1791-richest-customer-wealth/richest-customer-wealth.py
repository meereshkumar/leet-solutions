class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        max_wealth = 0 
        for customer in accounts:
            total = 0
            for money in customer:
                total += money
                max_wealth =max(max_wealth, total)
        return max_wealth