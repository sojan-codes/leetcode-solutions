class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        result = []
        val_max = max(candies)
        for i in range(len(candies)):
            candies[i] += extraCandies
            if candies[i] >= val_max:
                result.append(True)
            else:
                result.append(False)
        return result
