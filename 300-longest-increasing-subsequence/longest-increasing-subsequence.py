import bisect


class Solution:

    def lengthOfLIS(self, nums: list[int]) -> int:
        tails = []

        for num in nums:
            # Find the insertion index for num in tails
            idx = bisect.bisect_left(tails, num)

            # If num is larger than all elements in tails, append it
            if idx == len(tails):
                tails.append(num)
            # Otherwise, update tails[idx] to the smaller value num
            else:
                tails[idx] = num

        return len(tails)