class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n not in seen:
            sum = 0
            for i in str(n):
                sum = sum + (int(i)*int(i))
            if sum == 1:
                return True
            else:
                seen.add(n)
                n = sum
        return False