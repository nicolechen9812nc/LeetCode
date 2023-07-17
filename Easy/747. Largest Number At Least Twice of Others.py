#You are given an integer array nums where the largest integer is unique.

#Determine whether the largest element in the array is at least twice as much as every other number in the array. If it is, return the index of the largest element, or return -1 otherwise.

class Solution(object):
    def dominantIndex(self, nums):
        ind = nums.index(max(nums))
        nums.sort()
        if 2*nums[-2] <= nums[-1]:
            return ind
   
        return (-1)
