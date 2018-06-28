#!/usr/bin/env python

# given an array of integers, return the same array with the zeros moved at the end

class Solution:
    # two pointers with swapping O(n) time O(1) space
    def moveZeroesSlow(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        slow = 0
        fast = 0
        while fast < len(nums):
            while nums[slow] != 0:
                slow += 1
                if slow >= len(nums) - 1:
                    return
            fast = slow
            while nums[fast] == 0:
                fast += 1
                if fast >= len(nums):
                    return
            nums[slow], nums[fast] = nums[fast], nums[slow]
            
    # move all non zeros to beginning then pad with zeros, O(n) time O(1) space
    def moveZeroes(self, nums):
        non_zero_index = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[non_zero_index] = nums[i]
                non_zero_index += 1
        nums[non_zero_index:len(nums)] = [0] * (len(nums) - non_zero_index)
            
