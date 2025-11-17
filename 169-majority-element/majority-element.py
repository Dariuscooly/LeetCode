class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        index = {}

        for num in nums:
            index[num] = index.get(num, 0) + 1
        return max(index, key=index.get)