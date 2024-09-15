class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for point_a in range(len(nums)):
            for point_b in range(point_a + 1, len(nums)):
                if nums[point_a] + nums[point_b] == target:
                    return [point_a, point_b]
        return []