class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        ans = []
        for i in range(len(nums)):
            value = nums[nums[i]]
            ans.append(value)
        return ans
        