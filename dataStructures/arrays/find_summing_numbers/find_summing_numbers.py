#!/usr/bin/env python

#Given an array of integers, return indices of the two numbers such that they add up to a specific target.

#You may assume that each input would have exactly one solution, and you may not use the same element twice.

class Solution:
    # set O(n) O(n)
    def twoSum_set(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        complements = {}
        for i in range(len(nums)):
            if nums[i] in complements:
                return [complements[nums[i]], i]
            complements[target - nums[i]] = i
    
    # sort and two pointers O(nlogn) O(n)
    def twoSum(self, nums, target):
        left = 0
        right = len(nums) -1
        nums = sorted(zip(nums, range(len(nums))))
        while left < right:
            if nums[left][0] + nums[right][0] == target:
                return [nums[left][1], nums[right][1]]
            elif nums[left][0] + nums[right][0] > target:
                right -= 1
            elif nums[left][0] + nums[right][0] < target:
                left += 1
