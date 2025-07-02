import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()  # Convert to lowercase
        s = re.sub(r'[^a-z0-9]', '', s)  # Remove non-alphanumeric characters

        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True  # All characters matched
