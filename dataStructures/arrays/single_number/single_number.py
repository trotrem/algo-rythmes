#!/usr/bin/env python

# Given a non-empty array of integers, every element appears twice except for one. Find that single one.

class Solution:
    # sort O(nlogn) O(1)
    def singleNumber_sort(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        i = 0
        while i < len(nums):
            if i + 1 == len(nums) or nums[i] != nums[i + 1]:
                return nums[i]
            i+=2

    # set O(n) O(n/2)
    def singleNumber_set(self, nums):
        seen_once = set()
        for n in nums:
            if n not in seen_once:
                seen_once.add(n)
            else:
                seen_once.remove(n)
        return list(seen_once)[0]
    
    # xor O(n) O(1)
    def singleNumber(self, nums):
        scanner = 0
        for n in nums:
            scanner ^= n
        return scanner
    
    # naive O(n²) O(1)
