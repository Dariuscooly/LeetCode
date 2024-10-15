class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        output = [0] * n
        if k == 0:
            return output
        if k > 0:
            for i in range(n):
                output[i] = sum(code[(i + j) % n] for j in range(1, k + 1))
        elif k < 0:
            for i in range(n):
                output[i] = sum(code[(i + j) % n] for j in range(k, 0))
        return output

        