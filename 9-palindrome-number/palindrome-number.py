class Solution:
    def isPalindrome(self, x: int) -> bool: 
        val = str(x)
        right, left = len(val) - 1, 0

        while left < right:
            if val[left] != val[right]:
                return False
            left += 1
            right -= 1

        return True