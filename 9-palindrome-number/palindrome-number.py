class Solution:
    def isPalindrome(self, x: int) -> bool:
        val = str(x)
        rev = val[::-1]
        return val == rev


