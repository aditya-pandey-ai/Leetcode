class Solution:
    def plusOne(self, lst: List[int]) -> List[int]:

        number = int("".join(map(str, lst)))
        number += 1  
        new_list = [int(digit) for digit in str(number)]
        return new_list
