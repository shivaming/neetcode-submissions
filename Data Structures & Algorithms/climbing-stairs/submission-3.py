class Solution:
    def climbStairs(self, n: int) -> int:
        # We start with the answers for Step 0 and Step 1 already known.
        # 'one' represents our current step's answer.
        # 'two' represents the step right behind it.
        one = 1  # Ways to stay at Step 0
        two = 1  # Ways to get to Step 1
        
        # We need to calculate forward until we reach step 'n'.
        # The loop runs (n - 1) times to move us up the staircase.
        for i in range(n - 1):
            
            # Step A: Remember the current answer before we change it
            old_one = one
            
            # Step B: The rule! Next step = (Current step) + (Previous step)
            one = one + two
            
            # Step C: The old current step now becomes the 'previous' step
            two = old_one
            
        # Once the loop finishes, 'one' holds the total ways to reach the top!
        return one
