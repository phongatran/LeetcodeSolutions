class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Naive approach: test all possibilities until finding a match
        # This algorithm fails due to timeout
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i]+nums[j] == target:
                    return [i,j]
