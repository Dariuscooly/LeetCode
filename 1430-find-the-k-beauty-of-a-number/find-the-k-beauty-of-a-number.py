class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        output = 0
        lst = str(num)
        for i in range(len(lst) - k + 1):
            temp = int(lst[i:i+k])
            if temp != 0 and num % temp == 0:
                output += 1
        return output