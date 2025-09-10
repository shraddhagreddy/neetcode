#Contains duplicate
"""Contains Duplicate
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:

Input: nums = [1, 2, 3, 3]

Output: true

Example 2:

Input: nums = [1, 2, 3, 4]

Output: false"""



class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        l=1
        for r in range(1,len(nums)):
            if nums[r]!=nums[r-1]:
                nums[l]=nums[r]
                l=l+1
            else:
                return True
        return False