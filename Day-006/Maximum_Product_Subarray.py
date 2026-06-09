class Solution:
    def maxProduct(self, nums):
        n = len(nums)

        left_product = 1
        right_product = 1
        ans = nums[0]

        for i in range(n):
            if left_product == 0:
                left_product = 1
            if right_product == 0:
                right_product = 1

            # Prefix product
            left_product *= nums[i]

            # Suffix product
            right_product *= nums[n - 1 - i]

            ans = max(ans, left_product, right_product)

        return ans