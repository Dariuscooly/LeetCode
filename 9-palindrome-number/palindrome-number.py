class Solution:
    def isPalindrome(self, x: int) -> bool: 
        val = str(x)
        right, left = len(val) - 1, 0
        currentLength = len(val)

        while left < right and currentLength > 1:
            if val[left] != val[right]:
                return False
            left += 1
            right -= 1

        return True