class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        sum = 0
        temp = n
        while temp > 0:
            product *= temp % 10
            sum += temp % 10
            temp //= 10
        return product - sum