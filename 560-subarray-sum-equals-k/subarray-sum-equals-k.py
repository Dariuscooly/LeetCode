class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counter = 0
        prefix_sum = 0
        prefix_sum_count = defaultdict(int)
        prefix_sum_count[0] = 1  # Initialize with sum 0 to handle cases where the subarray starts from index 0
        
        for num in nums:
            prefix_sum += num
            # Check if there's a prefix_sum that, when subtracted from the current prefix_sum, equals k
            if (prefix_sum - k) in prefix_sum_count:
                counter += prefix_sum_count[prefix_sum - k]
            # Update the count of the current prefix_sum in the hash map
            prefix_sum_count[prefix_sum] += 1

        return counter