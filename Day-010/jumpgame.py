#55
class Solution:
    def canJump(self, nums):
        finalPosition = len(nums) - 1

        for idx in range(len(nums) - 2, -1, -1):
            if idx + nums[idx] >= finalPosition:
                finalPosition = idx

        return finalPosition == 0