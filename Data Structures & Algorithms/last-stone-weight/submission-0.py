class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.arr = stones
        
        while len(self.arr) > 1:
            self.arr.sort()
            if self.arr[len(self.arr)-1] == self.arr[len(self.arr)-2]:
                self.arr.pop()
                self.arr.pop()
            else:
                res = self.arr[len(self.arr)-1] - self.arr[len(self.arr)-2]
                self.arr.pop()
                self.arr.pop()
                self.arr.append(res)
        if len(self.arr) == 1:
            return self.arr[0]
        return 0
