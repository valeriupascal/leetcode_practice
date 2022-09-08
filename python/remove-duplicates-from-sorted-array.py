# Time:  O(n)
# Space: O(1)
#
# Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.
# 
# Do not allocate extra space for another array, you must do this in place with constant memory.
# 
# For example,
# Given input array A = [1,1,2],
# 
# Your function should return length = 2, and A is now [1,2].



class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
#         creating 2 pointers here 
        f, l = 0, 1
        while l < len(nums):
            if nums[f] != nums[l]:
                f += 1
                nums[f] = nums[l]
            l += 1
        return f + 1
