#!/usr/bin/env python
#Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

#Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.


class Solution(object):
    #two pointers O(N) time O(1) space
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        new_length = 1
        cur_index = 0
        # loop over array, swap array number, inc new_length on new number and set cur to new number index
        for i in range(1, len(nums)):
            if nums[i] != nums[cur_index]:
                nums[new_length] = nums[i]
                new_length += 1
                cur_index = i
        return new_length
        
