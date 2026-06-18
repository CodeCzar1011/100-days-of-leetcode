#49
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        if not strs:
            return []

        freq_map = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for ch in word:
                count[ord(ch) - ord('a')] += 1
            
            key = tuple(count)
            freq_map[key].append(word)

        return list(freq_map.values())