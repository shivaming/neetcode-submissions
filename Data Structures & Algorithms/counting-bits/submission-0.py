class Solution:
    def countBits(self, n: int) -> List[int]:
        count = []
        for num in range(n + 1):
            res = 0
            while num > 0:
                res += num % 2
                num = num >> 1
            count.append(res)
        return count

