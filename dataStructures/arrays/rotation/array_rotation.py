# rotate array nums right by k spaces

# 2. use swap cycles O(n) O(1)
# 3. use slices O(n) O(n)
class Solution(object):
    #slices: O(N) time, O(N) space
    def rotate_2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums[:] = nums[-(k % len(nums)):] + nums[:-(k % len(nums))]
    
    #swap cycles O(N) time, O(1) space     
    def rotate(self, nums, k):
        if k == 0 or k == len(nums):
            return
        rotation_count = 0
        start = 0
        cur = start
        next_index = (cur + k) % len(nums)
        temp = nums[cur]
        new_loop = True
        while rotation_count < len(nums):
            if cur != start or new_loop:
                new_loop = False
                temp, nums[next_index] = nums[next_index], temp
                cur = next_index
                rotation_count += 1
            else:
                new_loop = True
                start = (next_index + 1) % len(nums)
                cur = start
                temp = nums[cur]
            next_index = (cur + k) % len(nums)

    # other possibility: extend MutableSequence to create a shifted_array custom data structure O(1) O(1)
