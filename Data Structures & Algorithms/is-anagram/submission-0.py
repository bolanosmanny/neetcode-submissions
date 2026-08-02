class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = set()
        from collections import Counter

        return Counter(s) == Counter(t)


        