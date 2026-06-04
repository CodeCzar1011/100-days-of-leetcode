# ================================
# 3. HASHMAP (BEST METHOD 🚀)
# ================================
class Solution:
    def twoSum(self, nums, target):

        mpp = {}

        for i in range(len(nums)):

            more_needed = target - nums[i]

            if more_needed in mpp:
                return [mpp[more_needed], i]

            mpp[nums[i]] = i