class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def digit_sum(n):
            return sum(int(d) for d in str(n))  # Compute sum of digits
        
        digit_sum_map = {}  # Stores max number for each digit sum
        max_sum = -1

        for num in nums:
            ds = digit_sum(num)  # Calculate sum of digits
            
            if ds in digit_sum_map:
                max_sum = max(max_sum, num + digit_sum_map[ds])  # Update max sum
            
            digit_sum_map[ds] = max(digit_sum_map.get(ds, 0), num)  # Store max num for this digit sum

        return max_sum