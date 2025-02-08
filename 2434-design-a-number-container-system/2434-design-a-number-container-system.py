import heapq

class NumberContainers:
    def __init__(self):
        self.index_val = {}  # Maps index -> number
        self.res = {}  # Maps number -> min-heap of indices

    def change(self, index: int, number: int) -> None:
        if index in self.index_val:
            prevNum = self.index_val[index]
            if prevNum == number:
                return
            # Remove index from previous number's heap
            heapq.heappush(self.res[prevNum], -index)  # Mark as invalid (lazy deletion)

        # Add index to new number's heap
        if number not in self.res:
            self.res[number] = []
        heapq.heappush(self.res[number], index)

        # Update the index mapping
        self.index_val[index] = number

    def find(self, number: int) -> int:
        if number not in self.res or not self.res[number]:
            return -1

        # Remove invalid indices from the heap
        while self.res[number] and self.index_val.get(self.res[number][0]) != number:
            heapq.heappop(self.res[number])  # Lazy deletion

        return self.res[number][0] if self.res[number] else -1


# Example Usage:
# obj = NumberContainers()
# obj.change(1, 10)
# obj.change(2, 20)
# obj.change(1, 20)
# print(obj.find(10))  # Output: -1
# print(obj.find(20))  # Output: 1
