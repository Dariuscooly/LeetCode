class Solution:
    def isPalindrome(self, x: int) -> bool:
        num_list = [i for i in str(x)]
        return num_list == num_list[::-1] 