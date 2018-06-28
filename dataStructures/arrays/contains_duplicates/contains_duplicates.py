#!/usr/bin/env python

# given an array of integers, return True if it contaisn duplicates, False if not

class Solution(object):
    # set O(n) O(n)
    def containsDuplicate_set(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = set()
        for item in nums:
            if item not in seen:
                seen.add(item)
            else:
                return True
        return False
    
    # sort O(nlogn) O(1)
    def containsDuplicate(self, nums):
        if len(nums) < 2:
            return False
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False
