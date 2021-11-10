class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        N = len(nums) - 1
        for i in range(N):
            nums[i] = nums[i] * nums[i]
        nums.sort()
        return nums
