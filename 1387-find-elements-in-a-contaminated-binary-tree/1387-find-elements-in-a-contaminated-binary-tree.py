class FindElements:
    def __init__(self, root):
        self.root = root  # Store the reference to the root
    
    def find(self, target: int) -> bool:
        binary = bin(target + 1)[3:]  # Convert (target+1) to binary and remove the leading '1'
        index = 0
        root = self.root  # Pointer to traverse the tree
        
        while root and index < len(binary):  # Traverse the binary representation
            if binary[index] == '0':  # If 0, move left
                root = root.left
            else:  # If 1, move right
                root = root.right
            index += 1
        
        return root is not None  # If we reached the correct node, return True
