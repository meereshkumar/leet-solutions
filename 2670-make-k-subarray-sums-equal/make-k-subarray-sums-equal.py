import math


class Solution:

    def makeSubKSumEqual(self, arr: list[int], k: int) -> int:
        n = len(arr)
        g = math.gcd(n, k)
        ans = 0

        # Process each of the gcd(n, k) independent cycles
        for i in range(g):
            group = []
            j = i
            # Traverse all indices in the current cycle
            while arr[j] != -1:
                group.append(arr[j])
                arr[j] = -1  # Mark as visited
                j = (j + k) % n

            # Sort to find the median
            group.sort()
            median = group[len(group) // 2]

            # Accumulate minimum operations (distance to median)
            ans += sum(abs(x - median) for x in group)

        return ans