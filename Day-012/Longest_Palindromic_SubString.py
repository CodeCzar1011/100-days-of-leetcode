#5
class Solution:
    def longestPalindrome(self, s):
        lps = ""

        for i in range(len(s)):
            low = high = i

            while low >= 0 and high < len(s) and s[low] == s[high]:
                low -= 1
                high += 1

            if high - low - 1 > len(lps):
                lps = s[low + 1:high]

            low, high = i - 1, i

            while low >= 0 and high < len(s) and s[low] == s[high]:
                low -= 1
                high += 1

            if high - low - 1 > len(lps):
                lps = s[low + 1:high]

        return lps