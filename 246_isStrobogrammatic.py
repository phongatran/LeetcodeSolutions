class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        # Create a map to connect flippable numbers
        # Reject any number containing non-map digits
        # Create a flipped number
        # Output flipped number == number result
        
        map = {'0':'0','1':'1','6':'9','9':'6','8':'8'}
        
        new_number = []
        for i in reversed(num):
            if i not in map:
                return False
            new_number.append(map[i])
        
        new_number = "".join(new_number)
        return new_number == num
