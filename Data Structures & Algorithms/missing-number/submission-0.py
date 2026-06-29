class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0
        
        # 1. XOR all the numbers that SHOULD be in the list (0 to n)
        for i in range(n + 1):
            result ^= i
            
        # 2. XOR all the numbers that are ACTUALLY inside the list
        for num in nums:
            result ^= num
            
        # The numbers that match will turn to 0, leaving only the missing number
        return result
