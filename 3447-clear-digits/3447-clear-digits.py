class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        for char in s:
            if char.isdigit():
                if stack:  # Ensure stack is not empty before popping
                    stack.pop()
            else:
                stack.append(char)
    
        return ''.join(stack)