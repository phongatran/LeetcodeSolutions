class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Creates a table to rapidly retrieve index of the matched value in the original array.
        # Since the target is known, the complementary value is calculated.
        # If a match exists, then the complement value must exist within
        # the starting array. 
        # The last step returns the two indices
        
        hashtable = {}
        for i in range(len(nums)):
            hashtable[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashtable and hashtable[complement] != i:
                return [i,hashtable[complement]]
