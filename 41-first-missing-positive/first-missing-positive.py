class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        smallest = 1
        for n in nums:
            if n == smallest:
                smallest += 1
        return smallest  