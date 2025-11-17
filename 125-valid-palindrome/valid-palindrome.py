class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = [char.lower() for char in s if char.isalnum()]
        left, right = 0, len(x) - 1
        while left < right:
            print(f"Left -> {x[left]} == {x[right]} <- Right")
            if x[left] != x[right]:
                return False
            left += 1
            right -= 1
        return True