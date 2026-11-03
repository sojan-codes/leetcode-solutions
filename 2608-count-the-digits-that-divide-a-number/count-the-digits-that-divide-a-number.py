class Solution:
    def countDigits(self, num: int) -> int:
        num_str = [int(n) for n in str(num)]
        count = 0
        for i in range(len(num_str)):
            if num % num_str[i] == 0:
                count += 1
        return count
        