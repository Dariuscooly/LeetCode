class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        current_number = 0
        for current_number in range(len(nums)):
            if current_number not in nums:
                return current_number
        return current_number + 1
