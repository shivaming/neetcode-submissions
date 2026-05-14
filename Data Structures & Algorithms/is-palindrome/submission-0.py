class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = re.sub(r'[^a-zA-Z0-9]','',s.lower())
        #res = "".join(c for c in s.lower() if c.isalnum())
        return res[::-1]==res