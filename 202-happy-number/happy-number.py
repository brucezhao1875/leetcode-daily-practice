class Solution:
    def isHappy(self, n: int) -> bool:

        def get_sum_of_squares(n):
            return sum( int(digit)**2 for digit in str(n))

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_sum_of_squares(n)

        return n == 1 