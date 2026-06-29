class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        
        # We must loop exactly 32 times for a 32-bit integer
        for _ in range(32):
            # 1. Make room in our result by sliding its bits to the left
            result = result << 1
            
            # 2. Extract the last bit of 'n' and add it to our result
            result = result + (n % 2) # Using '|' or '+' works perfectly here
            
            # 3. Slide 'n' to the right to discard the bit we just processed
            n = n >> 1
            
        return result
