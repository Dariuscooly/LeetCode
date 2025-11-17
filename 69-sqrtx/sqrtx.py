class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        return int(x ** 0.5)
        