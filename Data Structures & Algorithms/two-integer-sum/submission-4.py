class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pMap = {} # number : index
        for idx,num in enumerate(nums):
            diff = target - num
            if diff in pMap and pMap[diff]!=idx:
                return [pMap[diff],idx]
            pMap[num]=idx #Add index of num