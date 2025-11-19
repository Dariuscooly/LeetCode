class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        from collections import defaultdict
        sorted_ = sorted(intervals)
        result = []
        index = {}
        for start, end in sorted_:
            if start in index:
                index[start] = max(index[start], end)
            else:
                index[start] = end

        current_start = None
        current_end = None

        for start, end in index.items():
            if current_start is None:
                current_start, current_end = start, end
            else:
                if start <= current_end:
                    current_end = max(current_end, end)
                else:
                    result.append([current_start,current_end])
                    current_start, current_end = start, end
            
        if current_start is not None:
            result.append([current_start,current_end])

        return result


