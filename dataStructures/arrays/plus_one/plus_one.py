#!/usr/bin/env python

# given an array of digits representing a non-negative integer, return the array representation of the integer plus one

class Solution:
    # paper addition: O(n) O(n) (average case O(n) O(1))
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        for i in reversed(range(len(digits))):
            if digits[i] + carry == 10:
                digits[i] = 0
            else:
                digits[i] += carry
                return digits
        return [1] + digits
