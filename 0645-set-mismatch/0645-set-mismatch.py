class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        count = Counter(nums)  # Count frequency of each number
        duplicate = missing = -1  # Initialize variables

        for i in range(1, n + 1):  # Check numbers from 1 to n
            if count[i] == 2:
                duplicate = i  # Found the duplicate number
            elif count[i] == 0:
                missing = i  # Found the missing number
            
        return [duplicate, missing]