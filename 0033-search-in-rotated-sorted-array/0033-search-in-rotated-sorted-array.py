class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1

        while start <= end:
            mid = (start + end) // 2

            # Check if mid is the target
            if nums[mid] == target:
                return mid

            # Identify which half is sorted
            if nums[start] <= nums[mid]:  # Left half is sorted
                if nums[start] <= target < nums[mid]:  # Target is in the sorted left half
                    end = mid - 1
                else:
                    start = mid + 1
            else:  # Right half is sorted
                if nums[mid] < target <= nums[end]:  # Target is in the sorted right half
                    start = mid + 1
                else:
                    end = mid - 1
        
        return -1  # Target not found
