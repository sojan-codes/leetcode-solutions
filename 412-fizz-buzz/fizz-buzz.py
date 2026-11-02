class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        result = []
        def check(i):
            if i % 3 == 0 and i % 5 == 0:
                return ("FizzBuzz")
            elif i % 3 == 0:
                return ("Fizz")
            elif i % 5 == 0:
                return ("Buzz")
            else:
                return (str(i))
        
        for i in range(1, n + 1):
            result.append(check(i))
        return result
            