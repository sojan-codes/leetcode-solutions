class Solution:
    def countDigits(self, num: int) -> int:
        count = 0
        temp = num
        while temp > 0:
            x = temp % 10
            if num % x == 0:
                count += 1
            temp //= 10
        return count
        