#88
class Solution:
    def merge(self, nums1, m, nums2, n):
        index = m

        # Copy all elements of nums2 into nums1
        for i in range(n):
            nums1[index] = nums2[i]
            index += 1

        # Sort nums1
        nums1.sort()