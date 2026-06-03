class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_to_open = { ')':'(','}':'{',']':'['}
        for b in s:
            if b in close_to_open:
                if stack:
                    top = stack.pop()
                else:
                    top = '#' #dummy
                if close_to_open[b] != top:
                    return False
            else:
                stack.append(b)
        return len(stack)==0