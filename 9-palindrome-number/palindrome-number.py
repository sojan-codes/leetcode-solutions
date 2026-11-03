class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = 0
        temp = x
        while temp > 0:
            n = temp % 10
            temp //= 10
            y = (y * 10 + n)
        
        return x == y

