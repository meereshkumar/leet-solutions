class Solution:
    def minEatingSpeed(self, piles, h):

        left = 1
        right = max(piles)

        while left < right:

            k = (left + right) // 2

            total_hours = 0

            for pile in piles:

                hours = (pile + k - 1) // k

                total_hours += hours

            if total_hours <= h:
                right = k

            else:
                left = k + 1

        return left