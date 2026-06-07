#238
def productExceptSelf(nums):
    n = len(nums)

    # Array to store all left multiplication
    left = [0] * n

    # Array to store all right multiplication
    right = [0] * n

    left[0] = 1
    for i in range(1, n):
        left[i] = left[i - 1] * nums[i - 1]

    right[n - 1] = 1
    for i in range(n - 2, -1, -1):
        right[i] = right[i + 1] * nums[i + 1]

    ans = [0] * n
    for i in range(n):
        ans[i] = left[i] * right[i]

    return ans