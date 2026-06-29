class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        
        for i in range(1, n + 1):
            # If the number is even: its answer is exactly the same as its half
            if i % 2 == 0:
                ans[i] = ans[i // 2]
            
            # If the number is odd: its answer is its half's answer + 1
            else:
                ans[i] = ans[i // 2] + 1
                
        return ans
