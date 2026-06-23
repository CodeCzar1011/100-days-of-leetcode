class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # If lengths differ, they can't be anagrams
        if len(s) != len(t):
            return False

        # Bucket for 26 lowercase letters
        counts = [0] * 26

        # Count characters in s
        for ch in s:
            counts[ord(ch) - ord('a')] += 1

        # Subtract characters in t
        for ch in t:
            counts[ord(ch) - ord('a')] -= 1

        # If any count is non‑zero, it's not an anagram
        for c in counts:
            if c != 0:
                return False
        return True