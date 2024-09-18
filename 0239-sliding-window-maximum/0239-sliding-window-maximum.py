class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = []
        left_side = 0
        retval = []
        for right_side in range(len(nums)):
            while queue and queue[-1] < nums[right_side]:
                queue.pop()
            queue.append(nums[right_side])
            if right_side + 1 >= k:
                retval.append(queue[0])
                if queue[0] == nums[left_side]:
                    queue.pop(0)
                left_side += 1
        return retval
        