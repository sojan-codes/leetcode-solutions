class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        result = []
        def check(n):
            count = 0
            for i in nums:
                if i < n:
                    count += 1
            return count

        for i in nums:
            result.append(check(i))
        return result
        