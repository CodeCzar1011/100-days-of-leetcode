#217
class Solution:
    def containsDuplicate(self, nums):
        int_set = set()

        for num in nums:
            if num in int_set:
                return True

            int_set.add(num)

        return False
