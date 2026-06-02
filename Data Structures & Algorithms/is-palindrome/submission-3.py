class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = re.sub(r'[^a-zA-Z0-9]','',s.lower())
        return t[::-1]==t