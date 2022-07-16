class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        #Create a Counter object from collections
        # Sort using two keys with the frequency being first and then
        # the opposite value of x to sort in decreasing order
        
        frequency = Counter(nums)
        return sorted(nums, key = lambda x: (frequency[x], -x))
