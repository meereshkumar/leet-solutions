class Solution:
    def isPalindrome(self, x: int) -> bool:
        total = 0
        xCopy = x
        while xCopy > 0:
            total *= 10 # 0 * 10
            total += xCopy%10 # 121 % 10 = 1
            xCopy = xCopy // 10 # 121 / 10 = 12
        
        return x == total
        