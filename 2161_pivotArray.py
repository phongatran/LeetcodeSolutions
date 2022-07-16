class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        # Create 3 arrays, one for the pivot, and two for the left and right sides
        # Then append accordingly while going through the list
        
        leftarray = []
        rightarray = []
        middlearray = []
        for i in range(len(nums)):
            if nums[i] < pivot:
                leftarray.append(nums[i])
            elif nums[i] > pivot:
                rightarray.append(nums[i])
            else:
                middlearray.append(nums[i])
        return leftarray + middlearray + rightarray
