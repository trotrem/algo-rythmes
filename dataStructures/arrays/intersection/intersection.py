#!/usr/bin/env python

# find the intersection of two integer arrays

import collections
class Solution:
    
    #count dictionaries O(n1 + n2) time O(k) space
    def intersect_dict(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dict1 = collections.defaultdict(int)
        dict2 = collections.defaultdict(int)
        for i in nums1:
            if i in dict1:
                dict1[i] += 1
            else:
                dict1[i] = 1
        for i in nums2:
            if i in dict2:
                dict2[i] += 1
            else:
                dict2[i] = 1
        intersection = []
        for i in dict1:
            for _ in range(min(dict1[i], dict2[i])):
                intersection.append(i)
        return intersection
    
    #Counter O(n1 + n2) time O(k) space
    def intersect_counter(self, nums1, nums2):
        return list((collections.Counter(nums1) & collections.Counter(nums2)).elements())
    
    
    #sort O(n1logn1 + n2logn2) time O(k) space
